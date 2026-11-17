"""
Export Module for InfluMatch Prototype
Generates structured Excel reports and WhatsApp-friendly text summaries.
"""
import io
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any

def export_to_excel(creators: List[Dict[str, Any]], campaign_meta: Dict[str, Any] = None) -> bytes:
    """
    Creates an Excel workbook (.xlsx) containing recommended creators and campaign brief metadata.
    Returns bytes buffer ready for Streamlit st.download_button.
    """
    campaign_meta = campaign_meta or {}
    output = io.BytesIO()

    # Format creator rows
    creator_rows = []
    for rank, c in enumerate(creators, 1):
        creator_rows.append({
            "Rank": rank,
            "Creator Name": c.get("creator_name", ""),
            "Handle": c.get("handle", ""),
            "Platform": c.get("platform", ""),
            "City": c.get("city", ""),
            "Follower Tier": c.get("follower_tier", ""),
            "Followers": c.get("follower_count", 0),
            "Primary Niche": c.get("primary_niche", ""),
            "Sub Niche": c.get("sub_niche", ""),
            "Overall Fit Score (%)": c.get("overall_fit", 0.0),
            "Topical Fit (%)": c.get("topical_fit", 0.0),
            "Community Fit (%)": c.get("community_fit", 0.0),
            "Style & Tone Fit (%)": c.get("style_fit", 0.0),
            "Commercial Tier Fit (%)": c.get("commercial_fit", 0.0),
            "Engagement Rate (%)": c.get("engagement_rate", 0.0),
            "Average Views": c.get("average_views", 0),
            "Commercial Pricing Tier": c.get("commercial_tier_pricing", ""),
            "Demo Profile Link": c.get("public_profile_link", "")
        })

    creators_df = pd.DataFrame(creator_rows)

    # Format metadata rows
    meta_rows = [
        {"Parameter": "Campaign Name", "Value": campaign_meta.get("campaign_name", "InfluMatch Campaign")},
        {"Parameter": "Export Date", "Value": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        {"Parameter": "Total Recommendations", "Value": len(creators)},
        {"Parameter": "Original Campaign Brief", "Value": campaign_meta.get("brief_text", "")},
        {"Parameter": "Detected Category", "Value": campaign_meta.get("category", "")},
        {"Parameter": "Target Persona", "Value": campaign_meta.get("target_persona", "")},
        {"Parameter": "Target Cities", "Value": ", ".join(campaign_meta.get("cities", []))},
        {"Parameter": "Target Platforms", "Value": ", ".join(campaign_meta.get("platforms", []))},
        {"Parameter": "Model Architecture", "Value": "InfluMatch 4-Factor Hybrid Rule/TF-IDF Engine (FYP Prototype)"}
    ]
    meta_df = pd.DataFrame(meta_rows)

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        creators_df.to_excel(writer, sheet_name="Recommended Creators", index=False)
        meta_df.to_excel(writer, sheet_name="Campaign Parameters", index=False)

    return output.getvalue()

def export_to_whatsapp_text(creators: List[Dict[str, Any]], campaign_name: str, brief_summary: str = "") -> str:
    """
    Generates a WhatsApp formatted markdown summary for quick agency sharing.
    """
    timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
    top_creators = creators[:5]

    lines = [
        f"*🎯 InfluMatch Shortlist: {campaign_name}*",
        f"📅 _{timestamp}_",
        ""
    ]

    if brief_summary:
        lines.append(f"📌 *Brief:* {brief_summary[:120]}...")
        lines.append("")

    lines.append("*🏆 Top Recommended Pakistani Creators:*")
    lines.append("────────────────────────")

    for i, c in enumerate(top_creators, 1):
        lines.append(f"*{i}. {c.get('creator_name')}* ({c.get('handle')})")
        lines.append(f"   📍 {c.get('city')} | 📱 {c.get('platform')} | 👥 {c.get('follower_tier')} ({c.get('follower_count', 0):,} followers)")
        lines.append(f"   ⭐ *Overall Match: {c.get('overall_fit')}%*")
        lines.append(f"   📊 Topical: {c.get('topical_fit')}% | Community: {c.get('community_fit')}% | Style: {c.get('style_fit')}%")
        lines.append(f"   💡 Focus: _{c.get('sub_niche')}_")
        lines.append("")

    lines.append("────────────────────────")
    lines.append("✨ _Generated via InfluMatch: Pakistan Creator Matching Engine_")

    return "\n".join(lines)
