"""
Explanations Module for InfluMatch Prototype
Generates grounded, feature-driven explanations for creator rankings.
Pre-TreeSHAP architecture designed to support LightGBM LambdaMART and SHAP values in FYP Phase 2.
"""
from typing import Dict, Any, List

def generate_match_explanation(creator: Dict[str, Any], extracted: Dict[str, Any]) -> str:
    """
    Synthesizes a transparent, feature-grounded explanation based on the creator's
    actual attribute match against campaign requirements.
    """
    reasons = []

    # 1. Topical alignment
    cat_match = extracted.get("category", "").lower() in creator.get("primary_niche", "").lower()
    if cat_match:
        reasons.append(
            f"their primary niche is **{creator.get('primary_niche')}** with verified content in **{creator.get('sub_niche')}**"
        )
    else:
        reasons.append(
            f"their content in **{creator.get('sub_niche')}** closely complements your campaign domain"
        )

    # 2. Tone and Style
    tone_req = extracted.get("tone", "Friendly")
    creator_tone = creator.get("content_tone", "Friendly")
    if tone_req == creator_tone:
        reasons.append(
            f"their **{creator_tone}** communication tone in {creator.get('language')} matches your exact tone preference"
        )
    else:
        reasons.append(
            f"their **{creator_tone}** tone aligns well with the campaign's {tone_req} objective"
        )

    # 3. Community / Persona
    city = creator.get("city", "")
    target_cities = extracted.get("cities", ["All Pakistan"])
    if "All Pakistan" in target_cities or city in target_cities:
        reasons.append(
            f"their audience base in **{city}** specifically reaches **{creator.get('audience_persona', 'targeted viewers')}**"
        )

    # 4. Commercial / Tier
    tier = creator.get("follower_tier", "Micro")
    target_tier = extracted.get("tier", "Micro")
    if tier == target_tier:
        reasons.append(
            f"their **{tier}** scale ({creator.get('follower_count', 0):,} followers) matches your target commercial tier"
        )

    explanation = (
        f"**Why this creator matches:**\n"
        f"This creator is a strong candidate because {reasons[0]}. "
        f"Furthermore, {reasons[1]}, and {reasons[2]}. "
        f"With an overall fit of **{creator.get('overall_fit', 0)}/100**, this creator provides grounded content credibility."
    )
    return explanation

def get_feature_contributions(creator: Dict[str, Any], weights: Dict[str, float] = None) -> List[Dict[str, Any]]:
    """
    Returns weighted point contribution for each factor (TreeSHAP proxy).
    Shows FYP evaluators how the final score is mathematically constructed.
    """
    from config import DEFAULT_WEIGHTS
    w = weights or DEFAULT_WEIGHTS

    topical_val = creator.get("topical_fit", 0.0)
    comm_val = creator.get("community_fit", 0.0)
    style_val = creator.get("style_fit", 0.0)
    tier_val = creator.get("commercial_fit", 0.0)

    return [
        {
            "dimension": "Topical Fit",
            "raw_score": topical_val,
            "weight": f"{int(w['topical']*100)}%",
            "points_contributed": round(topical_val * w["topical"], 2),
            "key_signal": f"Niche: {creator.get('primary_niche')} | Sub: {creator.get('sub_niche')}"
        },
        {
            "dimension": "Community / Persona Fit",
            "raw_score": comm_val,
            "weight": f"{int(w['community']*100)}%",
            "points_contributed": round(comm_val * w["community"], 2),
            "key_signal": f"City: {creator.get('city')} | Reach: {creator.get('audience_persona')[:40]}..."
        },
        {
            "dimension": "Style & Tone Fit",
            "raw_score": style_val,
            "weight": f"{int(w['style']*100)}%",
            "points_contributed": round(style_val * w["style"], 2),
            "key_signal": f"Tone: {creator.get('content_tone')} | Lang: {creator.get('language')}"
        },
        {
            "dimension": "Commercial Tier Fit",
            "raw_score": tier_val,
            "weight": f"{int(w['commercial']*100)}%",
            "points_contributed": round(tier_val * w["commercial"], 2),
            "key_signal": f"Tier: {creator.get('follower_tier')} ({creator.get('follower_count', 0):,} followers)"
        }
    ]
