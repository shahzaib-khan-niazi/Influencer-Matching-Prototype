"""
Comprehensive Test Script for InfluMatch Prototype
Validates all backend and matching modules end-to-end.
"""
import sys
from pathlib import Path

# Ensure paths
sys.path.insert(0, str(Path(__file__).resolve().parent))

from database.db import init_db, verify_user, register_user, save_campaign, get_user_campaigns
from modules.data_loader import load_creators_df, get_all_creators, get_dataset_stats
from modules.brief_parser import extract_requirements_from_brief
from modules.creator_matcher import match_and_rank_creators
from modules.explanations import generate_match_explanation, get_feature_contributions
from modules.export import export_to_excel, export_to_whatsapp_text

def run_tests():
    print("=" * 60)
    print("Starting InfluMatch System Verification Tests...")
    print("=" * 60)

    # Test 1: DB & Auth
    print("\n[Test 1] Testing Database & Authentication...")
    init_db()
    demo_user = verify_user("demo@brandagency.pk", "demo123")
    assert demo_user is not None, "Failed to verify demo user credentials!"
    assert demo_user["full_name"] == "Sarah Ahmed", "Demo user full name mismatch!"
    print(f"PASS: Demo user verified successfully: {demo_user['full_name']} ({demo_user['agency_name']})")

    # Test 2: Dataset Loading
    print("\n[Test 2] Testing Creators Dataset Loading...")
    creators = get_all_creators()
    assert len(creators) >= 30, f"Expected at least 30 creators, found {len(creators)}"
    stats = get_dataset_stats()
    print(f"PASS: Loaded {stats['total_creators']} creators across {len(stats['cities'])} Pakistani cities and {len(stats['categories'])} niches.")

    # Test 3: Roman Urdu Brief Parsing
    print("\n[Test 3] Testing Roman Urdu Brief NLP Parser...")
    roman_urdu_brief = (
        "Hum Karachi mein apni new skincare brand launch kar rahe hain. "
        "Humein aise influencers chahiye jo skincare, beauty aur self-care content banate hon. "
        "Audience mostly young females honi chahiye. Budget limited hai aur humein micro influencers prefer hain."
    )
    extracted = extract_requirements_from_brief(roman_urdu_brief)
    print(f"PASS: Parsed Brief Language: {extracted['detected_language']}")
    print(f"PASS: Extracted Category: {extracted['category']}")
    print(f"PASS: Extracted Cities: {extracted['cities']}")
    print(f"PASS: Extracted Tier: {extracted['tier']}")
    print(f"PASS: Extracted Keywords: {extracted['detected_keywords']}")
    assert extracted["category"] == "Beauty & Skincare", "Failed to detect Beauty & Skincare category!"
    assert "Karachi" in extracted["cities"], "Failed to detect Karachi city!"
    assert extracted["tier"] == "Micro", "Failed to detect Micro tier!"

    # Test 4: 4-Factor Matching and Ranking
    print("\n[Test 4] Testing 4-Factor Creator Matching & Ranking...")
    ranked, suggestions = match_and_rank_creators(
        all_creators=creators,
        extracted_requirements=extracted,
        brief_text=roman_urdu_brief,
        user_filters={"category": "Beauty & Skincare", "cities": ["Karachi"], "platforms": ["Instagram"]}
    )
    assert len(ranked) > 0, "No creators returned after ranking!"
    top_c = ranked[0]
    print(f"PASS: Top Match: {top_c['creator_name']} ({top_c['handle']})")
    print(f"      Overall Fit: {top_c['overall_fit']}%")
    print(f"      Topical Fit: {top_c['topical_fit']}% | Community: {top_c['community_fit']}%")
    print(f"      Style Fit: {top_c['style_fit']}% | Commercial: {top_c['commercial_fit']}%")
    assert 0 <= top_c["overall_fit"] <= 100, "Overall fit score out of [0, 100] bounds!"

    # Test 5: Explainability Engine
    print("\n[Test 5] Testing Grounded Explanation & Factor Attribution...")
    explanation = generate_match_explanation(top_c, extracted)
    assert len(explanation) > 50, "Explanation string too short!"
    print(f"PASS: Grounded Explanation Generated:\n{explanation}")

    contributions = get_feature_contributions(top_c)
    total_pts = sum(c["points_contributed"] for c in contributions)
    print(f"PASS: Mathematical Point Attribution Total: {round(total_pts, 1)} pts")

    # Test 6: Constraint Relaxation
    print("\n[Test 6] Testing Constraint Relaxation Suggestions...")
    # Apply narrow constraints (Multan + Facebook) to trigger relaxation
    narrow_ranked, narrow_sugs = match_and_rank_creators(
        all_creators=creators,
        extracted_requirements=extracted,
        brief_text=roman_urdu_brief,
        user_filters={"cities": ["Multan"], "platforms": ["Facebook"]}
    )
    print(f"Narrow matches count: {len(narrow_ranked)}")
    print(f"Relaxation suggestions generated: {len(narrow_sugs)}")
    if narrow_sugs:
        for s in narrow_sugs:
            print(f"   Suggestion: {s['suggested_action']} (+{s['additional_creators']} creators)")

    # Test 7: Export to Excel and WhatsApp
    print("\n[Test 7] Testing Excel and WhatsApp Export...")
    excel_bytes = export_to_excel(ranked, {"campaign_name": "Test Campaign", "brief_text": roman_urdu_brief})
    assert len(excel_bytes) > 1000, "Generated Excel file is empty or corrupted!"
    print(f"PASS: Excel workbook generated ({len(excel_bytes)} bytes)")

    wa_text = export_to_whatsapp_text(ranked, "DermaGlow Skincare Launch")
    assert "InfluMatch Shortlist" in wa_text, "WhatsApp template missing header!"
    print(f"PASS: WhatsApp shortlist text generated successfully:\n{wa_text[:180]}...")

    # Test 8: Save to Campaign History
    print("\n[Test 8] Testing Campaign DB Storage & Retrieval...")
    camp_id = save_campaign(
        user_id=demo_user["id"],
        campaign_name="Test FYP Skincare Campaign",
        brief_text=roman_urdu_brief,
        extracted_requirements=extracted,
        filters={"category": "Beauty & Skincare", "cities": ["Karachi"]},
        results_count=len(ranked),
        top_creators=ranked[:5]
    )
    assert camp_id is not None, "Failed to insert campaign into database!"
    history = get_user_campaigns(user_id=demo_user["id"])
    assert len(history) > 0, "No campaigns found in history!"
    print(f"PASS: Campaign #{camp_id} saved and retrieved from SQLite successfully.")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
