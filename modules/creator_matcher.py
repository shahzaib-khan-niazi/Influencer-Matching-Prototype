"""
Creator Matcher Module for InfluMatch Prototype
Executes hard filtering (platforms, cities), optional strict tier filtering,
calculates 4-factor ranking, and generates constraint relaxation suggestions.
"""
from typing import Dict, Any, List, Tuple
from modules.scoring import calculate_creator_scores
from config import DEFAULT_WEIGHTS

def evaluate_creator_pass_filters(creator: Dict[str, Any],
                                  selected_platforms: List[str],
                                  selected_cities: List[str],
                                  selected_tier: str,
                                  enforce_tier_strict: bool) -> bool:
    """Check if creator meets hard constraints."""
    # Platform filter
    if selected_platforms:
        if "All Platforms" not in selected_platforms and creator.get("platform") not in selected_platforms:
            return False

    # City filter
    if selected_cities:
        if "All Pakistan" not in selected_cities:
            if creator.get("city") not in selected_cities:
                return False

    # Tier strict filter
    if enforce_tier_strict and selected_tier and selected_tier != "Any Tier":
        tier_clean = selected_tier.split()[0]
        if creator.get("follower_tier") != tier_clean:
            return False

    return True

def analyze_constraint_relaxation(all_creators: List[Dict[str, Any]],
                                  selected_platforms: List[str],
                                  selected_cities: List[str],
                                  selected_tier: str,
                                  enforce_tier_strict: bool,
                                  current_match_count: int) -> List[Dict[str, Any]]:
    """
    Computes actionable relaxation suggestions when creator results are limited (< 3).
    Shows exact count changes so users can make informed trade-offs during live FYP demo.
    """
    suggestions = []

    # 1. Check City Relaxation
    if selected_cities and "All Pakistan" not in selected_cities:
        city_relaxed_count = sum(
            1 for c in all_creators
            if evaluate_creator_pass_filters(
                c, selected_platforms, ["All Pakistan"], selected_tier, enforce_tier_strict
            )
        )
        diff = city_relaxed_count - current_match_count
        if diff > 0:
            suggestions.append({
                "filter_name": "Geographic City Scope",
                "current_setting": ", ".join(selected_cities),
                "suggested_action": "Expand City Filter to 'All Pakistan'",
                "additional_creators": diff,
                "total_available": city_relaxed_count,
                "reason": f"Expanding beyond {', '.join(selected_cities)} unlocks {diff} high-affinity creators who have national Pakistani audience reach."
            })

    # 2. Check Platform Relaxation
    if selected_platforms and "All Platforms" not in selected_platforms and len(selected_platforms) < 4:
        plat_relaxed_count = sum(
            1 for c in all_creators
            if evaluate_creator_pass_filters(
                c, ["All Platforms"], selected_cities, selected_tier, enforce_tier_strict
            )
        )
        diff = plat_relaxed_count - current_match_count
        if diff > 0:
            suggestions.append({
                "filter_name": "Target Platform",
                "current_setting": ", ".join(selected_platforms),
                "suggested_action": "Enable Multi-Platform Search (e.g., add TikTok/YouTube)",
                "additional_creators": diff,
                "total_available": plat_relaxed_count,
                "reason": f"Broadening platform channels from {', '.join(selected_platforms)} introduces {diff} relevant Pakistani content creators."
            })

    # 3. Check Tier Relaxation (if strict)
    if enforce_tier_strict and selected_tier and selected_tier != "Any Tier":
        tier_relaxed_count = sum(
            1 for c in all_creators
            if evaluate_creator_pass_filters(
                c, selected_platforms, selected_cities, selected_tier, False
            )
        )
        diff = tier_relaxed_count - current_match_count
        if diff > 0:
            suggestions.append({
                "filter_name": "Follower Tier Strictness",
                "current_setting": f"Strict {selected_tier}",
                "suggested_action": "Switch Tier to Soft Preference (Allow Adjacent Tiers)",
                "additional_creators": diff,
                "total_available": tier_relaxed_count,
                "reason": f"Allowing adjacent commercial tiers with proportional scoring introduces {diff} potential matches."
            })

    return suggestions

def match_and_rank_creators(all_creators: List[Dict[str, Any]],
                           extracted_requirements: Dict[str, Any],
                           brief_text: str,
                           user_filters: Dict[str, Any] = None,
                           enforce_tier_strict: bool = False,
                           weights: Dict[str, float] = None) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Main matching pipeline:
    1. Filter creators based on hard constraints (platform, city, optional strict tier).
    2. Compute 4-factor scoring for all surviving candidates.
    3. Sort in descending order of Overall Fit Score.
    4. Compute constraint relaxation insights if pool is tight.
    """
    user_filters = user_filters or {}
    weights = weights or DEFAULT_WEIGHTS

    selected_platforms = user_filters.get("platforms", extracted_requirements.get("platforms", []))
    selected_cities = user_filters.get("cities", extracted_requirements.get("cities", ["All Pakistan"]))
    selected_tier = user_filters.get("tier", extracted_requirements.get("tier", "Micro"))

    qualifying_creators = []
    for creator in all_creators:
        if evaluate_creator_pass_filters(
            creator, selected_platforms, selected_cities, selected_tier, enforce_tier_strict
        ):
            scored_creator = calculate_creator_scores(
                creator, extracted_requirements, brief_text, weights
            )
            qualifying_creators.append(scored_creator)

    # Sort descending by overall fit
    ranked_creators = sorted(qualifying_creators, key=lambda x: x["overall_fit"], reverse=True)

    # Relaxation suggestions
    relaxation_suggestions = []
    if len(ranked_creators) < 4:
        relaxation_suggestions = analyze_constraint_relaxation(
            all_creators, selected_platforms, selected_cities, selected_tier,
            enforce_tier_strict, len(ranked_creators)
        )

    return ranked_creators, relaxation_suggestions
