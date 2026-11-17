"""
UI Components Module for InfluMatch Prototype
Provides standardized CSS styles, badges, progress bars, and creator cards.
Follows clean corporate aesthetic: White background, Navy blue (#1E3A8A) accents, minimal decorations.
"""
import streamlit as st
from config import THEME_COLORS
from modules.authentication import is_authenticated, get_current_user, logout

def apply_custom_styles():
    """Injects minimalist, clean CSS styling suitable for academic FYP defense."""
    st.markdown(
        f"""
        <style>
        /* Base page font and clean background */
        .stApp {{
            background-color: {THEME_COLORS['background']};
            color: {THEME_COLORS['text_dark']};
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}

        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: #FFFFFF;
            border-right: 1px solid {THEME_COLORS['border']};
        }}

        /* Clean Headers */
        h1, h2, h3, h4 {{
            color: {THEME_COLORS['primary_dark']};
            font-weight: 700;
        }}

        /* Buttons */
        .stButton>button {{
            background-color: {THEME_COLORS['primary']};
            color: #FFFFFF;
            border-radius: 6px;
            border: 1px solid {THEME_COLORS['primary_dark']};
            font-weight: 600;
            padding: 0.45rem 1rem;
            transition: background-color 0.15s ease;
        }}
        .stButton>button:hover {{
            background-color: {THEME_COLORS['secondary']};
            border-color: {THEME_COLORS['secondary']};
            color: #FFFFFF;
        }}

        /* Metric Cards */
        [data-testid="stMetricValue"] {{
            color: {THEME_COLORS['primary_dark']};
            font-weight: 700;
        }}

        /* Clean Card Container */
        .influ-card {{
            background-color: {THEME_COLORS['card_bg']};
            border: 1px solid {THEME_COLORS['border']};
            border-radius: 8px;
            padding: 1.25rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}

        /* Badges */
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.6rem;
            font-size: 0.78rem;
            font-weight: 600;
            border-radius: 4px;
            margin-right: 0.4rem;
        }}
        .badge-navy {{
            background-color: #EFF6FF;
            color: {THEME_COLORS['primary']};
            border: 1px solid #BFDBFE;
        }}
        .badge-gray {{
            background-color: #F1F5F9;
            color: {THEME_COLORS['text_muted']};
            border: 1px solid {THEME_COLORS['border']};
        }}
        .badge-green {{
            background-color: #DCFCE7;
            color: {THEME_COLORS['success']};
            border: 1px solid #BBF7D0;
        }}
        .badge-amber {{
            background-color: #FEF3C7;
            color: {THEME_COLORS['warning']};
            border: 1px solid #FDE68A;
        }}

        /* Progress Bar labels */
        .progress-label {{
            font-size: 0.82rem;
            color: {THEME_COLORS['text_muted']};
            margin-bottom: 2px;
            display: flex;
            justify-content: space-between;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def render_sidebar_user_profile():
    """Renders user info and session controls in sidebar."""
    with st.sidebar:
        st.markdown(
            f"""
            <div style="padding: 10px 0; border-bottom: 1px solid {THEME_COLORS['border']}; margin-bottom: 15px;">
                <h3 style="margin: 0; color: {THEME_COLORS['primary']}; font-size: 1.3rem;">⚡ InfluMatch</h3>
                <p style="margin: 2px 0 0 0; font-size: 0.8rem; color: {THEME_COLORS['text_muted']};">
                    Pakistan Creator Matching Engine
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if is_authenticated():
            user = get_current_user() or {}
            st.markdown(
                f"""
                <div style="background-color: #F8FAFC; border: 1px solid {THEME_COLORS['border']}; border-radius: 6px; padding: 10px; margin-bottom: 15px;">
                    <div style="font-size: 0.85rem; font-weight: 600; color: {THEME_COLORS['primary_dark']};">👤 {user.get('full_name', 'User')}</div>
                    <div style="font-size: 0.75rem; color: {THEME_COLORS['text_muted']};">{user.get('agency_name', 'Brand Agency')}</div>
                    <div style="font-size: 0.72rem; color: #94A3B8; margin-top: 2px;">{user.get('email', '')}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Log Out", key="sidebar_logout_btn", use_container_width=True):
                logout()
                st.rerun()
        else:
            st.info("Please log in to submit campaign briefs.")

def render_score_pill(score: float) -> str:
    """Returns an HTML badge for overall fit score."""
    if score >= 80:
        cls = "badge-green"
    elif score >= 60:
        cls = "badge-navy"
    else:
        cls = "badge-amber"
    return f'<span class="badge {cls}" style="font-size: 0.95rem; font-weight: 700;">★ {score}% Match</span>'
