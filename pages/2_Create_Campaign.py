"""
InfluMatch: Create Campaign / Submit Brief (Page 3)
Allows brand/agency users to submit Roman Urdu campaign briefs and structured filters.
Parses natural language requirements and triggers 4-factor creator matching.
"""
import streamlit as st
from config import (
    APP_NAME, THEME_COLORS, CATEGORIES, PLATFORMS, CITIES,
    CREATOR_TIERS, CAMPAIGN_SEASONS, CONTENT_TONES, BUDGET_PREFERENCES
)
from modules.authentication import init_auth_state, is_authenticated, get_current_user
from modules.ui_components import apply_custom_styles, render_sidebar_user_profile
from modules.brief_parser import extract_requirements_from_brief
from modules.data_loader import get_all_creators
from modules.creator_matcher import match_and_rank_creators
from database.db import save_campaign

st.set_page_config(page_title=f"Create Campaign | {APP_NAME}", page_icon="⚡", layout="wide")
init_auth_state()
apply_custom_styles()
render_sidebar_user_profile()

if not is_authenticated():
    st.warning("Please log in to submit a campaign brief.")
    if st.button("Go to Login Screen"):
        st.switch_page("app.py")
    st.stop()

user = get_current_user() or {}

st.markdown(
    f"""
    <div style="margin-bottom: 1.2rem;">
        <h1 style="color: {THEME_COLORS['primary_dark']}; margin-bottom: 0.2rem;">
            Create Campaign & Submit Brief
        </h1>
        <p style="color: {THEME_COLORS['text_muted']}; font-size: 1.05rem;">
            Enter your campaign brief in Roman Urdu, English, or mixed vernacular. InfluMatch will extract grounded parameters and match suitable creators.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Form Inputs
default_camp_name = st.session_state.get("form_campaign_name", "")
default_brief = st.session_state.get("form_brief", "")
default_cat = st.session_state.get("form_category", "Beauty & Skincare")
default_plat = st.session_state.get("form_platforms", ["Instagram", "TikTok"])
default_cities = st.session_state.get("form_cities", ["Karachi"])
default_tier = st.session_state.get("form_tier", "Micro (10K - 100K)")
default_season = st.session_state.get("form_season", "Summer")
default_tone = st.session_state.get("form_tone", "Friendly")
default_budget = st.session_state.get("form_budget", "Low (Nano / Micro Focus)")

with st.form("campaign_submission_form"):
    st.markdown("### A. Campaign Details & Free-Text Brief")
    camp_name = st.text_input("Campaign Name", value=default_camp_name, placeholder="e.g. Summer Skincare Campaign 2026")

    brief_text = st.text_area(
        "Campaign Brief (Accepts Roman Urdu, Urdu, English, or Mixed)",
        value=default_brief,
        height=140,
        placeholder="Hum Karachi mein apni new skincare brand launch kar rahe hain. Humein aise influencers chahiye jo skincare, beauty aur self-care content banate hon. Audience mostly young females honi chahiye. Budget limited hai aur humein micro influencers prefer hain."
    )

    st.markdown("### B. Structured Campaign Filters")
    col_f1, col_f2 = st.columns(2)

    with col_f1:
        cat_index = CATEGORIES.index(default_cat) if default_cat in CATEGORIES else 0
        selected_category = st.selectbox("Campaign Category", CATEGORIES, index=cat_index)

        selected_platforms = st.multiselect(
            "Target Platforms",
            PLATFORMS,
            default=[p for p in default_plat if p in PLATFORMS]
        )

        selected_cities = st.multiselect(
            "Target Cities (Select one or more, or All Pakistan)",
            CITIES,
            default=[c for c in default_cities if c in CITIES]
        )

        tier_index = CREATOR_TIERS.index(default_tier) if default_tier in CREATOR_TIERS else 2
        selected_tier = st.selectbox("Creator Follower Tier", CREATOR_TIERS, index=tier_index)

    with col_f2:
        season_index = CAMPAIGN_SEASONS.index(default_season) if default_season in CAMPAIGN_SEASONS else 0
        selected_season = st.selectbox("Campaign Season / Occasion", CAMPAIGN_SEASONS, index=season_index)

        tone_index = CONTENT_TONES.index(default_tone) if default_tone in CONTENT_TONES else 0
        selected_tone = st.selectbox("Preferred Content Tone", CONTENT_TONES, index=tone_index)

        budget_index = BUDGET_PREFERENCES.index(default_budget) if default_budget in BUDGET_PREFERENCES else 0
        selected_budget = st.selectbox("Budget Preference", BUDGET_PREFERENCES, index=budget_index)

        enforce_tier_strict = st.checkbox(
            "Enforce Tier as Strict Hard Filter (Default is Soft Preference)",
            value=False,
            help="If checked, creators outside this exact tier will be excluded rather than down-weighted."
        )

    submit_button = st.form_submit_button("🔍 Find Matching Creators", use_container_width=True)

if submit_button:
    if not brief_text.strip():
        st.error("Please enter a campaign brief before submitting.")
    else:
        with st.spinner("Analyzing brief with Roman Urdu NLP Lexicon & matching creators..."):
            user_filters = {
                "category": selected_category,
                "platforms": selected_platforms if selected_platforms else ["Instagram"],
                "cities": selected_cities if selected_cities else ["All Pakistan"],
                "tier": selected_tier,
                "season": selected_season,
                "tone": selected_tone,
                "budget": selected_budget
            }

            # 1. NLP Brief Analysis
            extracted_reqs = extract_requirements_from_brief(brief_text, user_filters)

            # 2. Match and Rank Creators
            all_creators = get_all_creators()
            ranked_results, relaxation_suggestions = match_and_rank_creators(
                all_creators=all_creators,
                extracted_requirements=extracted_reqs,
                brief_text=brief_text,
                user_filters=user_filters,
                enforce_tier_strict=enforce_tier_strict
            )

            # 3. Store in Session State
            st.session_state["current_campaign"] = {
                "campaign_name": camp_name,
                "brief_text": brief_text,
                "extracted_requirements": extracted_reqs,
                "filters": user_filters,
                "enforce_tier_strict": enforce_tier_strict
            }
            st.session_state["matching_results"] = ranked_results
            st.session_state["relaxation_suggestions"] = relaxation_suggestions

            # 4. Save to Database
            user_id = user.get("id", 1)
            save_campaign(
                user_id=user_id,
                campaign_name=camp_name,
                brief_text=brief_text,
                extracted_requirements=extracted_reqs,
                filters=user_filters,
                results_count=len(ranked_results),
                top_creators=ranked_results[:5]
            )

            # Navigate to Matching Results
            st.switch_page("pages/3_Matching_Results.py")
