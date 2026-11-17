"""
InfluMatch: Dashboard (Page 2)
Presents overview statistics, system workflow, and quick campaign launcher.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from config import APP_NAME, APP_SUBTITLE, THEME_COLORS
from modules.authentication import init_auth_state, is_authenticated, get_current_user
from modules.ui_components import apply_custom_styles, render_sidebar_user_profile
from modules.data_loader import load_creators_df, get_dataset_stats
from database.db import get_user_campaigns

st.set_page_config(page_title=f"Dashboard | {APP_NAME}", page_icon="⚡", layout="wide")
init_auth_state()
apply_custom_styles()
render_sidebar_user_profile()

if not is_authenticated():
    st.warning("Please log in to access the InfluMatch Dashboard.")
    if st.button("Go to Login Screen"):
        st.switch_page("app.py")
    st.stop()

user = get_current_user() or {}
stats = get_dataset_stats()
creators_df = load_creators_df()
recent_campaigns = get_user_campaigns(limit=5)

# Page Header
st.markdown(
    f"""
    <div style="margin-bottom: 1.5rem;">
        <h1 style="color: {THEME_COLORS['primary_dark']}; margin-bottom: 0.2rem;">
            Welcome to InfluMatch
        </h1>
        <p style="color: {THEME_COLORS['text_muted']}; font-size: 1.1rem; margin-top: 0;">
            {APP_SUBTITLE}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Statistics Overview
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Total Creators", f"{stats['total_creators']} PK Creators")
with m2:
    st.metric("Available Platforms", f"{len(stats['platforms'])} Platforms")
with m3:
    st.metric("Supported Categories", f"{len(stats['categories'])} Niches")
with m4:
    st.metric("Recent Campaign Searches", f"{len(recent_campaigns)} Searches")

st.markdown("---")

# Call to Action Banner
cta_col1, cta_col2 = st.columns([3, 1])
with cta_col1:
    st.markdown("### Ready to launch your Pakistani influencer campaign?")
    st.write("Submit a campaign brief in Roman Urdu or English to find matching verified creators.")
with cta_col2:
    st.write("")
    if st.button("🚀 Create New Campaign", use_container_width=True):
        st.switch_page("pages/2_Create_Campaign.py")

st.write("")

# How InfluMatch Works Section
st.markdown("### How InfluMatch Works")
w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown(
        f"""
        <div class="influ-card">
            <div style="font-size: 1.5rem; font-weight: 700; color: {THEME_COLORS['primary']}; margin-bottom: 8px;">01</div>
            <div style="font-weight: 700; color: {THEME_COLORS['primary_dark']}; margin-bottom: 6px;">Enter Campaign Brief</div>
            <div style="font-size: 0.85rem; color: {THEME_COLORS['text_muted']};">
                Input your brand requirements in Roman Urdu, English, or mixed language.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with w2:
    st.markdown(
        f"""
        <div class="influ-card">
            <div style="font-size: 1.5rem; font-weight: 700; color: {THEME_COLORS['primary']}; margin-bottom: 8px;">02</div>
            <div style="font-weight: 700; color: {THEME_COLORS['primary_dark']}; margin-bottom: 6px;">Analyze Requirements</div>
            <div style="font-size: 0.85rem; color: {THEME_COLORS['text_muted']};">
                NLP lexicon identifies category, target persona, city, and content tone.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with w3:
    st.markdown(
        f"""
        <div class="influ-card">
            <div style="font-size: 1.5rem; font-weight: 700; color: {THEME_COLORS['primary']}; margin-bottom: 8px;">03</div>
            <div style="font-weight: 700; color: {THEME_COLORS['primary_dark']}; margin-bottom: 6px;">Match Suitable Creators</div>
            <div style="font-size: 0.85rem; color: {THEME_COLORS['text_muted']};">
                4-Factor Fit algorithm ranks creators on Topical, Community, Style, and Commercial fit.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with w4:
    st.markdown(
        f"""
        <div class="influ-card">
            <div style="font-size: 1.5rem; font-weight: 700; color: {THEME_COLORS['primary']}; margin-bottom: 8px;">04</div>
            <div style="font-weight: 700; color: {THEME_COLORS['primary_dark']}; margin-bottom: 6px;">Review & Export</div>
            <div style="font-size: 0.85rem; color: {THEME_COLORS['text_muted']};">
                Inspect explainable factor scores, sample posts, and export to Excel / WhatsApp.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# Visualizations: Directory Distribution
st.markdown("### Pakistani Creator Directory Insights")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    niche_counts = creators_df["primary_niche"].value_counts().reset_index()
    niche_counts.columns = ["Niche", "Count"]
    fig_niche = px.bar(
        niche_counts,
        x="Count",
        y="Niche",
        orientation="h",
        title="Creators by Primary Niche",
        color_discrete_sequence=[THEME_COLORS["primary"]]
    )
    fig_niche.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        yaxis=dict(autorange="reversed")
    )
    st.plotly_chart(fig_niche, use_container_width=True)

with chart_col2:
    city_counts = creators_df["city"].value_counts().reset_index()
    city_counts.columns = ["City", "Count"]
    fig_city = px.pie(
        city_counts,
        names="City",
        values="Count",
        title="Creator Geographic Distribution Across Pakistan",
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig_city.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF"
    )
    st.plotly_chart(fig_city, use_container_width=True)
