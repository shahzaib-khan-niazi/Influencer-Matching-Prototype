"""
Database Module for InfluMatch Prototype
Handles SQLite storage for users and campaign search histories.
"""
import sqlite3
import hashlib
import json
from datetime import datetime
from pathlib import Path
from config import DATABASE_PATH, DATABASE_DIR, DEMO_CREDENTIALS

def hash_password(password: str) -> str:
    """Hash password using SHA-256 for basic prototype security."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def get_db_connection():
    """Create and return a database connection."""
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and seed demo user."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        agency_name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Campaigns Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        campaign_name TEXT NOT NULL,
        brief_text TEXT NOT NULL,
        extracted_requirements TEXT, -- JSON string
        filters TEXT,               -- JSON string
        results_count INTEGER DEFAULT 0,
        top_creator_names TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    # Seed Demo User
    demo_email = DEMO_CREDENTIALS["email"]
    cursor.execute("SELECT id FROM users WHERE email = ?", (demo_email,))
    existing_user = cursor.fetchone()
    if not existing_user:
        cursor.execute(
            """
            INSERT INTO users (email, password_hash, full_name, agency_name)
            VALUES (?, ?, ?, ?)
            """,
            (
                demo_email,
                hash_password(DEMO_CREDENTIALS["password"]),
                DEMO_CREDENTIALS["name"],
                DEMO_CREDENTIALS["agency"]
            )
        )

    conn.commit()
    conn.close()

def verify_user(email: str, password: str):
    """Verify user credentials. Returns user dict or None."""
    conn = get_db_connection()
    cursor = conn.cursor()
    pwd_hash = hash_password(password)
    cursor.execute(
        "SELECT id, email, full_name, agency_name FROM users WHERE email = ? AND password_hash = ?",
        (email.strip().lower(), pwd_hash)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def register_user(email: str, password: str, full_name: str, agency_name: str = ""):
    """Register a new user. Returns (success: bool, message: str, user_dict)."""
    email = email.strip().lower()
    if not email or not password or not full_name:
        return False, "Please fill in all required fields.", None

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        pwd_hash = hash_password(password)
        cursor.execute(
            """
            INSERT INTO users (email, password_hash, full_name, agency_name)
            VALUES (?, ?, ?, ?)
            """,
            (email, pwd_hash, full_name.strip(), agency_name.strip())
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return True, "Account created successfully! Please log in.", {
            "id": user_id,
            "email": email,
            "full_name": full_name,
            "agency_name": agency_name
        }
    except sqlite3.IntegrityError:
        conn.close()
        return False, "An account with this email already exists.", None
    except Exception as e:
        conn.close()
        return False, f"Registration error: {str(e)}", None

def save_campaign(user_id: int, campaign_name: str, brief_text: str,
                  extracted_requirements: dict, filters: dict,
                  results_count: int, top_creators: list):
    """Save a campaign search into history."""
    conn = get_db_connection()
    cursor = conn.cursor()
    top_names = ", ".join([c.get("creator_name", "") for c in top_creators[:5]])

    cursor.execute(
        """
        INSERT INTO campaigns (
            user_id, campaign_name, brief_text, extracted_requirements,
            filters, results_count, top_creator_names
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            campaign_name,
            brief_text,
            json.dumps(extracted_requirements),
            json.dumps(filters),
            results_count,
            top_names
        )
    )
    campaign_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return campaign_id

def get_user_campaigns(user_id: int = None, limit: int = 50):
    """Fetch campaigns history, ordered by newest first."""
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id:
        cursor.execute(
            """
            SELECT id, user_id, campaign_name, brief_text, extracted_requirements,
                   filters, results_count, top_creator_names, created_at
            FROM campaigns
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (user_id, limit)
        )
    else:
        cursor.execute(
            """
            SELECT id, user_id, campaign_name, brief_text, extracted_requirements,
                   filters, results_count, top_creator_names, created_at
            FROM campaigns
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,)
        )
    rows = cursor.fetchall()
    conn.close()

    campaigns = []
    for row in rows:
        item = dict(row)
        try:
            item["extracted_requirements"] = json.loads(item["extracted_requirements"])
        except Exception:
            item["extracted_requirements"] = {}
        try:
            item["filters"] = json.loads(item["filters"])
        except Exception:
            item["filters"] = {}
        campaigns.append(item)
    return campaigns

def get_campaign_by_id(campaign_id: int):
    """Fetch single campaign by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campaigns WHERE id = ?", (campaign_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    item = dict(row)
    try:
        item["extracted_requirements"] = json.loads(item["extracted_requirements"])
    except Exception:
        item["extracted_requirements"] = {}
    try:
        item["filters"] = json.loads(item["filters"])
    except Exception:
        item["filters"] = {}
    return item

# Automatically ensure DB is initialized on module load
init_db()
