"""
InfluMatch: A Roman Urdu Aware, Content Grounded Creator Matching Engine for Pakistan
Main Application Entry Point and Authentication Interface (Page 1)
"""
import streamlit as st
from config import APP_NAME, APP_TAGLINE, DEMO_CREDENTIALS, THEME_COLORS
from modules.authentication import init_auth_state, is_authenticated, login, sign_up, get_current_user
from modules.ui_components import apply_custom_styles, render_sidebar_user_profile

st.set_page_config(
    page_title=APP_NAME,
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
init_auth_state()
apply_custom_styles()
render_sidebar_user_profile()

def render_login_signup():
    """Renders the Page 1 Login / Sign Up interface."""
    col_center = st.columns([1, 2, 1])[1]

    with col_center:
        # App Header & Branding
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 1.5rem; margin-bottom: 2rem;">
                <div style="display: inline-block; background-color: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 50px; padding: 6px 18px; margin-bottom: 12px;">
                    <span style="color: {THEME_COLORS['primary']}; font-weight: 700; font-size: 0.85rem;">PAKISTAN CREATOR MATCHING ENGINE</span>
                </div>
                <h1 style="color: {THEME_COLORS['primary_dark']}; font-size: 2.4rem; margin-bottom: 0.4rem;">
                    ⚡ {APP_NAME}
                </h1>
                <p style="color: {THEME_COLORS['text_muted']}; font-size: 1.05rem; line-height: 1.5;">
                    {APP_TAGLINE}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        tab_login, tab_signup = st.tabs(["Agency Log In", "Create Account"])

        with tab_login:
            st.markdown("##### Log in to your Brand or Agency Account")

            default_email = st.session_state.get("login_email", "")
            default_pwd = st.session_state.get("login_password", "")

            with st.form("login_form"):
                email = st.text_input("Work Email Address", value=default_email, placeholder="e.g. yourname@brand.pk")
                password = st.text_input("Password", value=default_pwd, type="password")
                submit_login = st.form_submit_button("Log In to InfluMatch", use_container_width=True)

                if submit_login:
                    success, msg = login(email, password)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

        with tab_signup:
            st.markdown("##### Register New Agency Account")
            with st.form("signup_form"):
                reg_name = st.text_input("Full Name", placeholder="e.g. Asad Qureshi")
                reg_agency = st.text_input("Agency or Brand Name", placeholder="e.g. Starcom Pakistan")
                reg_email = st.text_input("Business Email", placeholder="e.g. asad@starcom.pk")
                reg_pwd = st.text_input("Password", type="password")
                submit_signup = st.form_submit_button("Create Account", use_container_width=True)

                if submit_signup:
                    success, msg = sign_up(reg_email, reg_pwd, reg_name, reg_agency)
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)

# Routing Logic
if not is_authenticated():
    render_login_signup()
else:
    # If user is already logged in, show welcome and navigation
    user = get_current_user() or {}
    st.markdown(
        f"""
        <div style="background-color: #FFFFFF; border: 1px solid {THEME_COLORS['border']}; border-radius: 8px; padding: 25px; margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h2 style="margin: 0; color: {THEME_COLORS['primary_dark']};">Welcome, {user.get('full_name', 'User')}</h2>
                    <p style="margin: 5px 0 0 0; color: {THEME_COLORS['text_muted']};">
                        Signed in as <b>{user.get('agency_name', 'Brand Agency')}</b> ({user.get('email')})
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📊 Dashboard")
        st.write("View creator directory stats, categories, and system overview.")
        if st.button("Open Dashboard", use_container_width=True):
            st.switch_page("pages/1_Dashboard.py")

    with col2:
        st.markdown("### ✍️ Create Campaign")
        st.write("Enter a Roman Urdu brief and run 4-factor creator matching.")
        if st.button("Create New Campaign", use_container_width=True):
            st.switch_page("pages/2_Create_Campaign.py")

    with col3:
        st.markdown("### 🕒 Campaign History")
        st.write("Review previous searches and reload previous match outputs.")
        if st.button("View Campaign History", use_container_width=True):
            st.switch_page("pages/4_Campaign_History.py")
