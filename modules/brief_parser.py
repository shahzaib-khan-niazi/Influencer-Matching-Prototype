"""
Brief Parser Module for InfluMatch Prototype
Extracts campaign requirements from mixed Roman Urdu, English, and Urdu briefs
using a structured Pakistani lexical rule-based matching engine.

Architecture Notice:
This module is designed as an interchangeable NLP component. For the FYP prototype,
it uses rule-based keyword mapping and semantic clustering. In the complete FYP pipeline,
this can be substituted with a fine-tuned MuRIL / EmbeddingGemma encoder.
"""
import re
from typing import Dict, Any, List

# Lexical mapping dictionaries for Pakistani Roman Urdu / English context
LEXICON = {
    "categories": {
        "Beauty & Skincare": [
            "skincare", "skin", "chehra", "jild", "makeup", "beauty", "glow", "cream",
            "serum", "acne", "danay", "keel", "sunscreen", "cosmetics", "face pack",
            "cleanser", "rang", "gora", "dermatology", "whitening", "spf"
        ],
        "Food & Dining": [
            "khana", "khabay", "food", "desi", "biryani", "nihari", "restaurant",
            "recipe", "pizzay", "chai", "nashta", "zaika", "cooking", "dhabas",
            "baking", "taste", "street food", "samosa", "roll", "karahi", "burger"
        ],
        "Fashion & Lifestyle": [
            "kapray", "fashion", "dress", "jora", "kurti", "designer", "wardrobe",
            "outfit", "lawn", "eid collection", "wedding", "shaadi", "bridal",
            "pret", "chappal", "styling", "aesthetic", "vlog", "thrift", "shoes"
        ],
        "Technology & Gadgets": [
            "tech", "technology", "mobile", "phone", "gadgets", "laptop", "unboxing",
            "specs", "camera", "software", "budget phone", "5g", "smartwatch",
            "earbuds", "pc", "pta", "gaming pc", "android", "iphone"
        ],
        "Fitness & Health": [
            "fitness", "sehat", "gym", "weight loss", "wazan", "diet", "kasrat",
            "bodybuilding", "workout", "exercise", "pcos", "hiking", "running",
            "healthy", "calories", "protein", "motapa"
        ],
        "Travel & Tourism": [
            "travel", "tourism", "safar", "trip", "tour", "northern areas", "hunza",
            "skardu", "beach", "road trip", "itinerary", "valleys", "swat", "kashmir"
        ],
        "Education & Career": [
            "taleem", "education", "study", "exam", "career", "university", "jobs",
            "freelancing", "coding", "skills", "css", "scholarship", "entry test",
            "upwork", "fiverr", "dollar earning"
        ],
        "Gaming & Esports": [
            "game", "gaming", "streamer", "pubg", "free fire", "pc gaming", "esports",
            "valorant", "gta", "clutch", "gameplay", "stream"
        ],
        "Parenting & Family": [
            "parenting", "family", "bachon", "bache", "kids", "moms", "mother",
            "toddler", "lunchbox", "school", "joint family", "parwarish"
        ],
        "Entertainment & Comedy": [
            "entertainment", "comedy", "funny", "mazahiya", "vines", "prank",
            "parody", "sketch", "humor", "haspatal", "acting", "mimicry"
        ]
    },
    "cities": {
        "Karachi": ["karachi", "khi", "clifton", "defence", "burns road", "gulshan"],
        "Lahore": ["lahore", "lhr", "gulberg", "dha lahore", "anarkali", "walled city"],
        "Islamabad": ["islamabad", "isb", "margalla", "f-7", "f-6", "blue area"],
        "Rawalpindi": ["rawalpindi", "pindi", "saddar pindi", "kartarpura"],
        "Faisalabad": ["faisalabad", "fsd", "clock tower", "lyallpur"],
        "Hyderabad": ["hyderabad", "hyd", "latifabad", "sindh university"],
        "Multan": ["multan", "cantt multan", "hussain agahi"],
        "Peshawar": ["peshawar", "namak mandi", "hayatabad", "kpk"]
    },
    "platforms": {
        "Instagram": ["instagram", "insta", "ig", "reels", "stories", "grid"],
        "TikTok": ["tiktok", "tik tok", "tt", "short videos"],
        "YouTube": ["youtube", "yt", "vlogs", "long form", "subscribers"],
        "Facebook": ["facebook", "fb", "meta", "page"]
    },
    "tiers": {
        "Nano": ["nano", "chotay", "beginner", "chotay creators", "1k", "5k"],
        "Micro": ["micro", "micro influencers", "micro creators", "10k", "50k"],
        "Mid": ["mid", "mid-tier", "darmiyanay", "growing creators", "100k", "200k"],
        "Macro": ["macro", "big creators", "bary creators", "famous", "500k"],
        "Mega": ["mega", "celebrity", "top tier", "million", "superstar"]
    },
    "seasons": {
        "Ramadan": ["ramadan", "ramzan", "sehri", "iftar", "roza", "barkat"],
        "Eid": ["eid", "chand raat", "eid ul fitr", "eid ul adha", "bakra eid"],
        "Wedding Season (Shaadi)": ["wedding", "shaadi", "shadi", "barat", "walima", "mehendi", "bridal", "dulhan"],
        "PSL / Cricket": ["psl", "cricket", "match", "pakistan super league", "lahore qalandars", "karachi kings"],
        "Winter": ["winter", "sardi", "thand", "winter collection"],
        "Summer": ["summer", "garmi", "garmiyan", "lawn"]
    },
    "tones": {
        "Friendly": ["friendly", "dostana", "warm", "approachable", "pyara"],
        "Informative": ["informative", "maloomati", "guide", "honest review", "educational", "saboot"],
        "Humorous / Entertaining": ["funny", "humor", "humorous", "mazahiya", "comedy", "entertaining", "hasnay"],
        "Professional": ["professional", "formal", "clinical", "serious", "expert", "doctor"],
        "Casual & Desi": ["casual", "desi", "asli", "raw", "daily routine", "sadah"],
        "Inspirational / Aspirational": ["inspirational", "aspirational", "luxury", "aesthetic", "glamorous", "dream"]
    },
    "budgets": {
        "Low": ["low budget", "limited budget", "kam budget", "sasta", "pocket friendly", "economical", "munasib"],
        "Medium": ["medium budget", "darmiyana budget", "standard budget", "balanced budget"],
        "High": ["high budget", "ziada budget", "unlimited", "premium budget", "corporate"]
    }
}

ROMAN_URDU_MARKERS = [
    "hum", "apni", "karein", "chahiye", "aur", "mein", "ke liye", "hona",
    "wali", "hota", "hai", "hain", "kar rahe", "humein", "aise", "jo", "hon",
    "bohat", "achha", "paratha", "kapray", "sehat", "bhi", "lekin"
]

def detect_language(text: str) -> str:
    """Identify if the text is predominantly Roman Urdu, Urdu script, English, or Mixed."""
    urdu_chars = len(re.findall(r'[\u0600-\u06FF]', text))
    text_lower = text.lower()
    roman_urdu_count = sum(1 for word in ROMAN_URDU_MARKERS if re.search(rf'\b{word}\b', text_lower))

    if urdu_chars > 15:
        return "Urdu (Nastaliq / Arabic Script)"
    elif roman_urdu_count >= 2:
        return "Roman Urdu (Pakistan Vernacular)"
    elif any(word in text_lower for word in ["skincare", "launch", "brand", "agency", "influencers"]):
        return "Mixed (Roman Urdu & English)"
    return "English"

def extract_requirements_from_brief(brief_text: str, user_filters: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Parses a free-text campaign brief in Roman Urdu/English and merges with structured filters.
    Returns structured analysis object for UI and ranking models.
    """
    text_lower = brief_text.lower()
    user_filters = user_filters or {}

    detected_keywords: List[str] = []

    # 1. Category extraction
    detected_category = None
    category_scores = {}
    for cat, kw_list in LEXICON["categories"].items():
        score = sum(1 for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower))
        if score > 0:
            category_scores[cat] = score
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])

    if category_scores:
        detected_category = max(category_scores, key=category_scores.get)
    category = user_filters.get("category") or detected_category or "Beauty & Skincare"

    # 2. City extraction
    detected_cities = []
    for city, kw_list in LEXICON["cities"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_cities.append(city)
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])

    if user_filters.get("cities"):
        cities = user_filters["cities"]
    elif detected_cities:
        cities = detected_cities
    else:
        cities = ["All Pakistan"]

    # 3. Platform extraction
    detected_platforms = []
    for plat, kw_list in LEXICON["platforms"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_platforms.append(plat)
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])

    if user_filters.get("platforms"):
        platforms = user_filters["platforms"]
    elif detected_platforms:
        platforms = detected_platforms
    else:
        platforms = ["Instagram"]

    # 4. Creator Tier extraction
    detected_tier = None
    for tier, kw_list in LEXICON["tiers"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_tier = tier
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])
            break

    filter_tier = user_filters.get("tier")
    if filter_tier and filter_tier != "Any Tier":
        # Extract base tier name (e.g., 'Micro' from 'Micro (10K - 100K)')
        target_tier = filter_tier.split()[0]
    else:
        target_tier = detected_tier or "Micro"

    # 5. Tone extraction
    detected_tone = None
    for tone, kw_list in LEXICON["tones"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_tone = tone
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])
            break
    tone = user_filters.get("tone") or detected_tone or "Friendly"

    # 6. Seasonality extraction
    detected_season = None
    for season, kw_list in LEXICON["seasons"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_season = season
            detected_keywords.extend([kw for kw in kw_list if re.search(rf'\b{re.escape(kw)}\b', text_lower)])
            break
    season = user_filters.get("season") or detected_season or "General / Ongoing"

    # 7. Budget extraction
    detected_budget = None
    for b_lvl, kw_list in LEXICON["budgets"].items():
        if any(re.search(rf'\b{re.escape(kw)}\b', text_lower) for kw in kw_list):
            detected_budget = b_lvl
            break
    filter_budget = user_filters.get("budget")
    if filter_budget:
        budget = filter_budget.split()[0]
    else:
        budget = detected_budget or ("Low" if target_tier in ["Nano", "Micro"] else "Medium")

    # 8. Target Persona & Audience extraction
    audience_clues = []
    if any(w in text_lower for w in ["female", "females", "larkian", "women", "khawateen", "girls"]):
        audience_clues.append("Young Females (18-28)")
    elif any(w in text_lower for w in ["male", "males", "larke", "boys", "men"]):
        audience_clues.append("Young Males (18-35)")

    if any(w in text_lower for w in ["students", "university", "college", "hostel"]):
        audience_clues.append("College & University Students")
    if any(w in text_lower for w in ["budget", "affordable", "sasta", "pocket"]):
        audience_clues.append("Price-sensitive consumer segment")
    if any(w in text_lower for w in ["luxury", "premium", "bridal"]):
        audience_clues.append("High-intent bridal & luxury shoppers")

    target_persona = ", ".join(audience_clues) if audience_clues else "Broad Pakistani Consumer Demographic"

    language_detected = detect_language(brief_text)

    # Sub-niche deduction based on keywords
    sub_niche = "General " + category
    if "skincare" in text_lower or "serum" in text_lower or "acne" in text_lower:
        sub_niche = "Affordable Skincare & Daily Routines"
    elif "biryani" in text_lower or "street food" in text_lower:
        sub_niche = "Street Food & Local Eateries"
    elif "gadgets" in text_lower or "mobile" in text_lower:
        sub_niche = "Budget Smartphones & Consumer Tech"
    elif "lawn" in text_lower or "eid" in text_lower:
        sub_niche = "Festive Lawn & Ready-to-wear Outfits"
    elif "pcos" in text_lower or "weight loss" in text_lower:
        sub_niche = "Desi Weight Loss & Hormonal Health"

    return {
        "category": category,
        "sub_niche": sub_niche,
        "target_persona": target_persona,
        "cities": cities if isinstance(cities, list) else [cities],
        "platforms": platforms if isinstance(platforms, list) else [platforms],
        "tone": tone,
        "tier": target_tier,
        "season": season,
        "budget": budget,
        "detected_language": language_detected,
        "detected_keywords": sorted(list(set(detected_keywords))),
        "parser_model": "Roman Urdu Lexical Parser (Pre-MuRIL Architecture)"
    }
