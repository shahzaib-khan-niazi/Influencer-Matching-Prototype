"""
InfluMatch Configuration File
Central configuration for UI themes, weights, taxonomy, and database paths.
"""
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "influmatch.db"
CREATORS_CSV_PATH = DATA_DIR / "creators.csv"

# App Branding
APP_NAME = "InfluMatch"
APP_TAGLINE = "A Roman Urdu Aware, Content Grounded Creator Matching Engine for Pakistan"
APP_SUBTITLE = "Find the right Pakistani creators for your next campaign with explainable fit scoring."

# Demo Credentials for FYP Presentation
DEMO_CREDENTIALS = {
    "email": "demo@brandagency.pk",
    "password": "demo123",
    "name": "Sarah Ahmed",
    "agency": "Zenith PR & Brand Agency"
}

# Theme Colors (Professional Light Theme with Navy Accents)
THEME_COLORS = {
    "primary": "#1E3A8A",      # Navy Blue
    "primary_dark": "#0F2454", # Deep Navy
    "secondary": "#2563EB",    # Royal Blue
    "accent": "#0D9488",       # Teal accent
    "background": "#F8FAFC",   # Soft slate-white
    "card_bg": "#FFFFFF",      # Pure White
    "border": "#E2E8F0",       # Light gray
    "text_dark": "#0F172A",    # Slate dark
    "text_muted": "#64748B",   # Slate gray
    "success": "#16A34A",      # Green
    "warning": "#D97706",      # Amber
    "danger": "#DC2626"        # Red
}

# 4-Factor Scoring Weights (Default Formula from FYP Spec)
DEFAULT_WEIGHTS = {
    "topical": 0.40,
    "community": 0.25,
    "style": 0.20,
    "commercial": 0.15
}

# Taxonomy & Filter Options for Pakistani Creator Ecosystem
CATEGORIES = [
    "Beauty & Skincare",
    "Fashion & Lifestyle",
    "Food & Dining",
    "Technology & Gadgets",
    "Fitness & Health",
    "Travel & Tourism",
    "Education & Career",
    "Gaming & Esports",
    "Parenting & Family",
    "Entertainment & Comedy"
]

PLATFORMS = [
    "Instagram",
    "TikTok",
    "YouTube",
    "Facebook"
]

CITIES = [
    "All Pakistan",
    "Karachi",
    "Lahore",
    "Islamabad",
    "Rawalpindi",
    "Faisalabad",
    "Hyderabad",
    "Multan",
    "Peshawar"
]

CREATOR_TIERS = [
    "Any Tier",
    "Nano (1K - 10K)",
    "Micro (10K - 100K)",
    "Mid (100K - 500K)",
    "Macro (500K - 1M)",
    "Mega (1M+)"
]

CAMPAIGN_SEASONS = [
    "General / Ongoing",
    "Ramadan",
    "Eid",
    "Wedding Season (Shaadi)",
    "PSL / Cricket",
    "Winter",
    "Summer",
    "Independence Day (Azadi)"
]

CONTENT_TONES = [
    "Friendly",
    "Informative",
    "Humorous / Entertaining",
    "Professional",
    "Casual & Desi",
    "Inspirational / Aspirational"
]

BUDGET_PREFERENCES = [
    "Low (Nano / Micro Focus)",
    "Medium (Micro / Mid Focus)",
    "High (Mid / Macro / Mega Focus)"
]
