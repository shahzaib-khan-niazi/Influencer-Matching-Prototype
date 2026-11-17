"""
InfluMatch: Campaign History (Page 9)
Displays previous campaign searches stored in local SQLite database.
Allows agency users to review historical briefs and reload past results.
"""
import streamlit as st
import pandas as pd
from config import APP_NAME, THEME_COLORS
from modules.authentication import init_auth_state, is_authenticated, get_current_user
from modules.ui_components import apply_custom_styles, render_sidebar_user_profile
from database.db import get_user_campaigns, get_campaign_by_id
from modules.data_loader import get_all_creators
from modules.creator_matcher import match_and_rank_creators

st.set_page_config(page_title=f"Campaign History | {APP_NAME}", page_icon="⚡", layout="wide")
init_auth_state()
apply_custom_styles()
render_sidebar_user_profile()

if not is_authenticated():
    st.warning("Please log in to view your campaign history.")
    if st.button("Go to Login Screen"):
        st.switch_page("app.py")
    st.stop()

user = get_current_user() or {}
campaigns = get_user_campaigns(user_id=user.get("id"))

st.markdown(
    f"""
    <div style="margin-bottom: 1.2rem;">
        <h1 style="color: {THEME_COLORS['primary_dark']}; margin-bottom: 0.2rem;">
            Campaign Search History
        </h1>
        <p style="color: {THEME_COLORS['text_muted']}; font-size: 1.05rem;">
            Audit trail of previously submitted briefs. Click any campaign to reload results.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

if not campaigns:
    st.info("No campaign searches recorded yet. Create your first campaign to build history.")
    if st.button("Create New Campaign"):
        st.switch_page("pages/2_Create_Campaign.py")
else:
    st.write(f"Showing **{len(campaigns)}** saved campaign searches:")

    for idx, camp in enumerate(campaigns, 1):
        with st.container():
            st.markdown(
                f"""
                <div class="influ-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                        <div>
                            <span style="font-size: 1.15rem; font-weight: 700; color: {THEME_COLORS['primary_dark']};">
                                #{idx} {camp.get('campaign_name')}
                            </span>
                            <div style="font-size: 0.8rem; color: {THEME_COLORS['text_muted']}; margin-top: 3px;">
                                📅 Saved on: {camp.get('created_at')} &nbsp;|&nbsp; Matches: <b>{camp.get('results_count')} Creators</b>
                            </div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            col_details, col_action = st.columns([3, 1])

            with col_details:
                reqs = camp.get("extracted_requirements", {})
                st.markdown(f"**Brief:** *\"{camp.get('brief_text', '')[:140]}...\"*")
                st.markdown(
                    f"**Extracted Params:** `{reqs.get('category', 'N/A')}` &nbsp;|&nbsp; "
                    f"Cities: `{', '.join(reqs.get('cities', ['All Pakistan']))}` &nbsp;|&nbsp; "
                    f"Platforms: `{', '.join(reqs.get('platforms', ['Instagram']))}`"
                )
                if camp.get("top_creator_names"):
                    st.caption(f"Top Matches: {camp.get('top_creator_names')}")

            with col_action:
                st.write("")
                if st.button(f"🔄 Reload Results", key=f"reload_camp_{camp.get('id')}", use_container_width=True):
                    with st.spinner("Reloading campaign matching results..."):
                        all_c = get_all_creators()
                        brief_text = camp.get("brief_text", "")
                        extracted_reqs = camp.get("extracted_requirements", {})
                        filters = camp.get("filters", {})

                        ranked_results, relaxation_suggestions = match_and_rank_creators(
                            all_creators=all_c,
                            extracted_requirements=extracted_reqs,
                            brief_text=brief_text,
                            user_filters=filters,
                            enforce_tier_strict=False
                        )

                        st.session_state["current_campaign"] = {
                            "campaign_name": camp.get("campaign_name"),
                            "brief_text": brief_text,
                            "extracted_requirements": extracted_reqs,
                            "filters": filters,
                            "enforce_tier_strict": False
                        }
                        st.session_state["matching_results"] = ranked_results
                        st.session_state["relaxation_suggestions"] = relaxation_suggestions
                        st.switch_page("pages/3_Matching_Results.py")

            st.write("")
