"""
Data Loader Module for InfluMatch Prototype
Loads and caches the Pakistani creator dataset and provides helper functions.
"""
import json
import pandas as pd
from pathlib import Path
from config import CREATORS_CSV_PATH

try:
    import streamlit as st
    cache_decorator = st.cache_data
except ImportError:
    def cache_decorator(func):
        return func

@cache_decorator
def load_creators_df() -> pd.DataFrame:
    """Load creators dataset from CSV into a clean pandas DataFrame."""
    if not CREATORS_CSV_PATH.exists():
        raise FileNotFoundError(f"Creators dataset not found at {CREATORS_CSV_PATH}")

    df = pd.read_csv(CREATORS_CSV_PATH)

    # Parse JSON captions safely
    def parse_captions(val):
        if isinstance(val, str):
            try:
                return json.loads(val)
            except Exception:
                return [val]
        elif isinstance(val, list):
            return val
        return []

    df["sample_post_captions"] = df["sample_post_captions"].apply(parse_captions)
    return df

def get_all_creators():
    """Returns list of creator dicts."""
    df = load_creators_df()
    return df.to_dict(orient="records")

def get_creator_by_id(creator_id: str):
    """Fetch a single creator dictionary by creator_id."""
    df = load_creators_df()
    match = df[df["creator_id"] == creator_id]
    if not match.empty:
        return match.iloc[0].to_dict()
    return None

def get_dataset_stats():
    """Returns summary statistics for the dashboard."""
    df = load_creators_df()
    return {
        "total_creators": len(df),
        "platforms": df["platform"].unique().tolist(),
        "categories": df["primary_niche"].unique().tolist(),
        "cities": df["city"].unique().tolist(),
        "tiers": df["follower_tier"].unique().tolist(),
        "avg_engagement": round(df["engagement_rate"].mean(), 2)
    }
