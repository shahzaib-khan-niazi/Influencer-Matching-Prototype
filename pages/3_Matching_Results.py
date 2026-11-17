"""
InfluMatch: Matching Results Page (Page 6, 7, 8 & 10)
Displays extracted campaign requirements, ranked creators with 4-factor fit bars,
constraint relaxation suggestions, detailed profile inspector, and Excel/WhatsApp export.
"""
import streamlit as st
from config import APP_NAME, THEME_COLORS
from modules.authentication import init_auth_state, is_authenticated
from modules.ui_components import apply_custom_styles, render_sidebar_user_profile, render_score_pill
from modules.export import export_to_excel, export_to_whatsapp_text
from modules.creator_matcher import match_and_rank_creators
from modules.data_loader import get_all_creators

st.set_page_config(page_title=f"Matching Results | {APP_NAME}", page_icon="⚡", layout="wide")
init_auth_state()
apply_custom_styles()
render_sidebar_user_profile()

if not is_authenticated():
    st.warning("Please log in to view campaign results.")
    if st.button("Go to Login Screen"):
        st.switch_page("app.py")
    st.stop()

# Check if we have active campaign results
if "current_campaign" not in st.session_state or "matching_results" not in st.session_state:
    st.info("No active campaign search found. Please submit a campaign brief first.")
    if st.button("Create New Campaign"):
        st.switch_page("pages/2_Create_Campaign.py")
    st.stop()

campaign = st.session_state["current_campaign"]
results = st.session_state["matching_results"]
relaxation_suggestions = st.session_state.get("relaxation_suggestions", [])
extracted = campaign.get("extracted_requirements", {})

# Page Title
st.markdown(
    f"""
    <div style="margin-bottom: 1.2rem;">
        <h1 style="color: {THEME_COLORS['primary_dark']}; margin-bottom: 0.2rem;">
            Creator Recommendations & Matching Results
        </h1>
        <p style="color: {THEME_COLORS['text_muted']}; font-size: 1.05rem;">
            Campaign: <b>{campaign.get('campaign_name', 'InfluMatch Campaign')}</b> &nbsp;|&nbsp; Found <b>{len(results)}</b> matching creators ranked by 4-factor fit score.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------
# Section 1: Campaign Summary & NLP Extraction Analysis
# -------------------------------------------------------------
with st.expander("📋 Submitted Brief & Extracted Campaign Requirements", expanded=True):
    col_brief, col_extracted = st.columns([1.1, 1.3])

    with col_brief:
        st.markdown("##### Original Campaign Brief")
        st.markdown(
            f"""
            <div style="background-color: #F8FAFC; border: 1px solid {THEME_COLORS['border']}; border-left: 4px solid {THEME_COLORS['primary']}; border-radius: 6px; padding: 12px 16px; font-style: italic; color: #334155;">
                "{campaign.get('brief_text', '')}"
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(f"**Detected Input Language:** `{extracted.get('detected_language', 'Roman Urdu')}`")
        if extracted.get("detected_keywords"):
            st.markdown(f"**Extracted Lexical Anchors:** `{'`, `'.join(extracted.get('detected_keywords', [])[:8])}`")

    with col_extracted:
        st.markdown("##### Extracted Campaign Parameters (NLP Analysis)")
        p1, p2 = st.columns(2)
        with p1:
            st.markdown(f"**Primary Category:** `{extracted.get('category')}`")
            st.markdown(f"**Deduced Sub-Niche:** `{extracted.get('sub_niche')}`")
            st.markdown(f"**Target Persona:** `{extracted.get('target_persona')}`")
            st.markdown(f"**Target Cities:** `{', '.join(extracted.get('cities', []))}`")
        with p2:
            st.markdown(f"**Required Platforms:** `{', '.join(extracted.get('platforms', []))}`")
            st.markdown(f"**Preferred Content Tone:** `{extracted.get('tone')}`")
            st.markdown(f"**Campaign Season:** `{extracted.get('season')}`")
            st.markdown(f"**Commercial Tier / Budget:** `{extracted.get('tier')} ({extracted.get('budget')} budget)`")

        st.caption("Architecture note: Rule-based Roman Urdu semantic parser ready for MuRIL transformer integration.")

# -------------------------------------------------------------
# Section 2: Constraint Relaxation Suggestions (If pool is tight)
# -------------------------------------------------------------
if relaxation_suggestions:
    st.markdown(
        f"""
        <div style="background-color: #FFFBEB; border: 1px solid #FCD34D; border-left: 4px solid #F59E0B; border-radius: 6px; padding: 14px 18px; margin: 15px 0;">
            <div style="font-weight: 700; color: #92400E; font-size: 0.95rem; margin-bottom: 6px;">
                ⚠️ CONSTRAINT RELAXATION ADVISORY ({len(results)} Creators Currently Matched)
            </div>
            <div style="font-size: 0.86rem; color: #78350F;">
                Your hard filters resulted in a narrow creator shortlist. InfluMatch computed the following relaxation opportunities:
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for i, sug in enumerate(relaxation_suggestions):
        col_sug_text, col_sug_action = st.columns([3, 1])
        with col_sug_text:
            st.markdown(f"**Option {i+1}: {sug['suggested_action']}**")
            st.write(f"• Impact: **+{sug['additional_creators']} more creators** (Total {sug['total_available']} available)")
            st.caption(f"Reason: {sug['reason']}")
        with col_sug_action:
            st.write("")
            if st.button(f"Apply Option {i+1}", key=f"relax_btn_{i}"):
                # Apply relaxation dynamically
                filters = campaign.get("filters", {})
                if sug["filter_name"] == "Geographic City Scope":
                    filters["cities"] = ["All Pakistan"]
                    extracted["cities"] = ["All Pakistan"]
                elif sug["filter_name"] == "Target Platform":
                    filters["platforms"] = ["Instagram", "TikTok", "YouTube", "Facebook"]
                    extracted["platforms"] = ["Instagram", "TikTok", "YouTube", "Facebook"]
                elif sug["filter_name"] == "Follower Tier Strictness":
                    campaign["enforce_tier_strict"] = False

                all_c = get_all_creators()
                new_results, new_sugs = match_and_rank_creators(
                    all_c, extracted, campaign["brief_text"], filters, campaign.get("enforce_tier_strict", False)
                )
                st.session_state["matching_results"] = new_results
                st.session_state["relaxation_suggestions"] = new_sugs
                st.rerun()

# -------------------------------------------------------------
# Section 3: Recommended Creators (Top 10 Cards)
# -------------------------------------------------------------
st.write("")
top_creators = results[:10]

col_header_l, col_header_r = st.columns([2, 1])
with col_header_l:
    st.markdown(f"### Top {len(top_creators)} Recommended Creators")
with col_header_r:
    st.write("")
    # Quick jump to export section
    st.markdown(
        f'<div style="text-align: right; color: {THEME_COLORS["text_muted"]}; font-size: 0.85rem;">'
        f'Formula: <b>Topical (40%) + Community (25%) + Style (20%) + Commercial (15%)</b>'
        f'</div>',
        unsafe_allow_html=True
    )

if not top_creators:
    st.error("No creators match your current hard constraints. Please click 'Create New Campaign' or relax filters above.")
else:
    for idx, creator in enumerate(top_creators, 1):
        with st.container():
            st.markdown(
                f"""
                <div class="influ-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                        <div>
                            <span style="font-size: 1.15rem; font-weight: 700; color: {THEME_COLORS['primary_dark']};">
                                #{idx} {creator.get('creator_name')}
                            </span>
                            <span style="color: {THEME_COLORS['text_muted']}; font-size: 0.9rem; margin-left: 6px;">
                                {creator.get('handle')}
                            </span>
                            <div style="margin-top: 6px;">
                                <span class="badge badge-navy">📍 {creator.get('city')}</span>
                                <span class="badge badge-gray">📱 {creator.get('platform')}</span>
                                <span class="badge badge-gray">👥 {creator.get('follower_tier')} ({creator.get('follower_count', 0):,} followers)</span>
                                <span class="badge badge-gray">🎯 {creator.get('primary_niche')}</span>
                            </div>
                        </div>
                        <div style="text-align: right; margin-top: 4px;">
                            {render_score_pill(creator.get('overall_fit', 0.0))}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # 4 Dimension Progress Bars
            sub1, sub2 = st.columns(2)
            with sub1:
                st.markdown(
                    f'<div class="progress-label"><span>Topical Fit (40%)</span><b>{creator.get("topical_fit")}%</b></div>',
                    unsafe_allow_html=True
                )
                st.progress(creator.get("topical_fit", 0.0) / 100.0)

                st.markdown(
                    f'<div class="progress-label" style="margin-top: 6px;"><span>Community / Persona Fit (25%)</span><b>{creator.get("community_fit")}%</b></div>',
                    unsafe_allow_html=True
                )
                st.progress(creator.get("community_fit", 0.0) / 100.0)

            with sub2:
                st.markdown(
                    f'<div class="progress-label"><span>Style & Tone Fit (20%)</span><b>{creator.get("style_fit")}%</b></div>',
                    unsafe_allow_html=True
                )
                st.progress(creator.get("style_fit", 0.0) / 100.0)

                st.markdown(
                    f'<div class="progress-label" style="margin-top: 6px;"><span>Commercial Tier Fit (15%)</span><b>{creator.get("commercial_fit")}%</b></div>',
                    unsafe_allow_html=True
                )
                st.progress(creator.get("commercial_fit", 0.0) / 100.0)

            st.write("")

# -------------------------------------------------------------
# Section 4: Exporting (Requirement 10)
# -------------------------------------------------------------
st.markdown("---")
st.markdown("### 📤 Export Campaign Shortlist")
exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    st.markdown("##### 1. Export to Excel (.xlsx)")
    st.write("Download structured workbook with creator scores, handles, contact metrics, and campaign brief.")
    excel_data = export_to_excel(
        creators=results,
        campaign_meta={
            "campaign_name": campaign.get("campaign_name", "InfluMatch Campaign"),
            "brief_text": campaign.get("brief_text", ""),
            "category": extracted.get("category", ""),
            "target_persona": extracted.get("target_persona", ""),
            "cities": extracted.get("cities", []),
            "platforms": extracted.get("platforms", [])
        }
    )
    st.download_button(
        label="📥 Download Excel Report",
        data=excel_data,
        file_name=f"InfluMatch_{campaign.get('campaign_name', 'Shortlist').replace(' ', '_')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

with exp_col2:
    st.markdown("##### 2. WhatsApp-Friendly Shortlist")
    st.write("Quick text formatted for immediate sharing in client or PR agency WhatsApp groups.")
    wa_text = export_to_whatsapp_text(
        creators=results,
        campaign_name=campaign.get("campaign_name", "InfluMatch Shortlist"),
        brief_summary=campaign.get("brief_text", "")
    )
    st.text_area("Copy-Paste Shortlist Text:", value=wa_text, height=130)
