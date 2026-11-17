"""
Scoring Module for InfluMatch Prototype
Calculates the 4-factor fit scores for Pakistani creators against campaign requirements:
1. Topical Fit (40%)
2. Community / Persona Fit (25%)
3. Style & Tone Fit (20%)
4. Commercial Tier Fit (15%)

Uses Scikit-learn TF-IDF text similarity combined with rule-based attribute scoring.
"""
import re
from typing import Dict, Any, List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config import DEFAULT_WEIGHTS

TIER_ORDER = {
    "Nano": 0,
    "Micro": 1,
    "Mid": 2,
    "Macro": 3,
    "Mega": 4
}

TONE_COMPATIBILITY = {
    "Friendly": ["Friendly", "Casual & Desi", "Informative"],
    "Informative": ["Informative", "Professional", "Friendly"],
    "Humorous / Entertaining": ["Humorous / Entertaining", "Casual & Desi", "Friendly"],
    "Professional": ["Professional", "Informative"],
    "Casual & Desi": ["Casual & Desi", "Friendly", "Humorous / Entertaining"],
    "Inspirational / Aspirational": ["Inspirational / Aspirational", "Professional", "Friendly"]
}

def compute_text_similarity(doc1: str, doc2: str) -> float:
    """Compute TF-IDF cosine similarity between two text strings [0.0 - 1.0]."""
    if not doc1.strip() or not doc2.strip():
        return 0.0
    try:
        vectorizer = TfidfVectorizer(stop_words=None, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
        sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(sim)
    except Exception:
        return 0.0

def compute_topical_fit(creator: Dict[str, Any], extracted: Dict[str, Any], brief_text: str) -> float:
    """
    Computes Topical Fit (0-100):
    Evaluates primary niche alignment, sub-niche overlap, and TF-IDF similarity of captions.
    """
    req_cat = extracted.get("category", "")
    creator_niche = creator.get("primary_niche", "")
    
    # Base niche alignment
    if req_cat.lower() in creator_niche.lower() or creator_niche.lower() in req_cat.lower():
        niche_score = 60.0
    else:
        # Check partial intersection
        tokens_cat = set(req_cat.lower().split())
        tokens_niche = set(creator_niche.lower().split())
        if tokens_cat.intersection(tokens_niche):
            niche_score = 40.0
        else:
            niche_score = 15.0

    # Corpus of creator text
    captions = " ".join(creator.get("sample_post_captions", []))
    creator_corpus = f"{creator.get('primary_niche', '')} {creator.get('sub_niche', '')} {creator.get('content_description', '')} {captions}".lower()

    # Match with brief and detected keywords
    keywords_text = " ".join(extracted.get("detected_keywords", []))
    query_text = f"{brief_text} {extracted.get('sub_niche', '')} {keywords_text}".lower()

    tfidf_sim = compute_text_similarity(query_text, creator_corpus)
    text_score = min(35.0, tfidf_sim * 70.0)

    # Keyword intersection bonus
    kw_hits = 0
    for kw in extracted.get("detected_keywords", []):
        if re.search(rf'\b{re.escape(kw)}\b', creator_corpus):
            kw_hits += 1
    keyword_bonus = min(15.0, kw_hits * 3.0)

    total_topical = niche_score + text_score + keyword_bonus
    return round(min(100.0, max(0.0, total_topical)), 1)

def compute_community_fit(creator: Dict[str, Any], extracted: Dict[str, Any]) -> float:
    """
    Computes Community / Persona Fit (0-100):
    Evaluates target audience demographic overlap, gender focus, and city alignment.
    """
    score = 30.0 # base score
    target_persona = extracted.get("target_persona", "").lower()
    creator_persona = creator.get("audience_persona", "").lower()
    creator_desc = creator.get("content_description", "").lower()
    combined_persona = f"{creator_persona} {creator_desc}"

    # Demographic & gender markers
    if "female" in target_persona or "women" in target_persona or "larkian" in target_persona:
        if any(w in combined_persona for w in ["women", "female", "girls", "brides", "mothers", "moms"]):
            score += 25.0
        elif any(w in combined_persona for w in ["men", "boys", "gents"]):
            score -= 10.0
    elif "male" in target_persona or "men" in target_persona or "larke" in target_persona:
        if any(w in combined_persona for w in ["men", "boys", "gents", "gamers", "youth"]):
            score += 25.0
        elif any(w in combined_persona for w in ["women", "female", "girls"]):
            score -= 10.0

    # Student / youth alignment
    if "student" in target_persona or "university" in target_persona:
        if any(w in combined_persona for w in ["student", "university", "college", "hostel", "pocket-money"]):
            score += 15.0

    # City geographic alignment
    target_cities = [c.lower() for c in extracted.get("cities", ["All Pakistan"])]
    creator_city = creator.get("city", "").lower()

    if "all pakistan" in target_cities or not target_cities:
        score += 20.0
    elif creator_city in target_cities:
        score += 30.0
    else:
        # Different city
        score += 5.0

    return round(min(100.0, max(0.0, score)), 1)

def compute_style_fit(creator: Dict[str, Any], extracted: Dict[str, Any]) -> float:
    """
    Computes Style & Tone Fit (0-100):
    Evaluates tone compatibility, language alignment, and seasonal relevance.
    """
    target_tone = extracted.get("tone", "Friendly")
    creator_tone = creator.get("content_tone", "Friendly")

    # Tone scoring
    if target_tone == creator_tone:
        tone_score = 55.0
    elif creator_tone in TONE_COMPATIBILITY.get(target_tone, []):
        tone_score = 40.0
    else:
        tone_score = 25.0

    # Language alignment
    creator_lang = creator.get("language", "").lower()
    detected_lang = extracted.get("detected_language", "").lower()
    if "roman urdu" in detected_lang and "roman urdu" in creator_lang:
        lang_score = 30.0
    elif "english" in detected_lang and "english" in creator_lang:
        lang_score = 28.0
    else:
        lang_score = 20.0

    # Seasonality relevance bonus
    season = extracted.get("season", "General / Ongoing")
    captions = " ".join(creator.get("sample_post_captions", [])).lower()
    season_score = 0.0
    if season != "General / Ongoing":
        season_token = season.split()[0].lower()
        if season_token in captions or season_token in creator.get("content_description", "").lower():
            season_score = 15.0
        else:
            season_score = 8.0
    else:
        season_score = 15.0

    total_style = tone_score + lang_score + season_score
    return round(min(100.0, max(0.0, total_style)), 1)

def compute_commercial_fit(creator: Dict[str, Any], extracted: Dict[str, Any]) -> float:
    """
    Computes Commercial Tier Fit (0-100):
    Evaluates follower tier distance and budget compatibility.
    """
    target_tier = extracted.get("tier", "Micro")
    creator_tier = creator.get("follower_tier", "Micro")
    budget = extracted.get("budget", "Medium")

    # Tier distance penalty
    t_target_idx = TIER_ORDER.get(target_tier, 1)
    t_creator_idx = TIER_ORDER.get(creator_tier, 1)
    diff = abs(t_target_idx - t_creator_idx)

    if diff == 0:
        tier_score = 60.0
    elif diff == 1:
        tier_score = 45.0
    elif diff == 2:
        tier_score = 25.0
    else:
        tier_score = 10.0

    # Budget alignment
    pricing = creator.get("commercial_tier_pricing", "Medium")
    if budget == "Low":
        if pricing == "Low":
            budget_score = 40.0
        elif pricing == "Medium":
            budget_score = 25.0
        else:
            budget_score = 10.0
    elif budget == "High":
        if pricing in ["Medium", "High"]:
            budget_score = 40.0
        else:
            budget_score = 25.0
    else: # Medium
        if pricing == "Medium":
            budget_score = 40.0
        elif pricing == "Low":
            budget_score = 35.0
        else:
            budget_score = 25.0

    total_comm = tier_score + budget_score
    return round(min(100.0, max(0.0, total_comm)), 1)

def calculate_creator_scores(creator: Dict[str, Any], extracted: Dict[str, Any],
                             brief_text: str, weights: Dict[str, float] = None) -> Dict[str, Any]:
    """
    Calculates all 4 fit scores and the weighted overall fit score.
    Returns creator dict enriched with score breakdown.
    """
    w = weights or DEFAULT_WEIGHTS

    topical = compute_topical_fit(creator, extracted, brief_text)
    community = compute_community_fit(creator, extracted)
    style = compute_style_fit(creator, extracted)
    commercial = compute_commercial_fit(creator, extracted)

    overall = (
        (topical * w["topical"]) +
        (community * w["community"]) +
        (style * w["style"]) +
        (commercial * w["commercial"])
    )
    overall = round(min(100.0, max(0.0, overall)), 1)

    result = dict(creator)
    result["topical_fit"] = topical
    result["community_fit"] = community
    result["style_fit"] = style
    result["commercial_fit"] = commercial
    result["overall_fit"] = overall
    return result
