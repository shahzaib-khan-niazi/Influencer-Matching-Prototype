"""
Authentication Module for InfluMatch Prototype
Handles session state management, login, logout, and registration logic.
"""
import streamlit as st
from database.db import verify_user, register_user, DEMO_CREDENTIALS

def init_auth_state():
    """Ensure authentication keys exist in st.session_state."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None

def is_authenticated() -> bool:
    """Check if current session is authenticated."""
    return st.session_state.get("authenticated", False)

def get_current_user():
    """Return dict of current logged in user or None."""
    return st.session_state.get("user", None)

def login(email: str, password: str):
    """Attempt login with email and password."""
    user = verify_user(email, password)
    if user:
        st.session_state["authenticated"] = True
        st.session_state["user"] = user
        return True, "Login successful!"
    return False, "Invalid email or password. Please check your credentials."

def logout():
    """Clear user session state."""
    st.session_state["authenticated"] = False
    st.session_state["user"] = None
    if "current_campaign" in st.session_state:
        del st.session_state["current_campaign"]
    if "matching_results" in st.session_state:
        del st.session_state["matching_results"]

def sign_up(email: str, password: str, full_name: str, agency_name: str = ""):
    """Attempt account registration."""
    success, message, user = register_user(email, password, full_name, agency_name)
    return success, message
