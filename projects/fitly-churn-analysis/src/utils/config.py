from pathlib import Path

# ==========================================
# 1. PROJECT ROOT (The Anchor)
# ==========================================
# This dynamically finds your project root, no matter where you run code from.
# We go up 3 levels: config.py -> utils -> src -> PROJECT_ROOT
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# ==========================================
# 2. DIRECTORY STRUCTURE
# ==========================================
# Define your main folders relative to the root
DATA_DIR = PROJECT_ROOT / "data"
FIGURES_DIR = PROJECT_ROOT / "images"  # or "figures"


# ==========================================
# 3. FILE PATHS (The "Config" part)
# ==========================================
# Use pathlib's "/" operator to join paths cleanly

# Input Data (Raw)
RAW_DATA_DIR = DATA_DIR / "raw"
ACCOUNT_INFO_PATH = RAW_DATA_DIR / "da_fitly_account_info.csv"
CUSTOMER_SUPPORT_PATH = RAW_DATA_DIR / "da_fitly_customer_support.csv"
USER_ACTIVITY_PATH = RAW_DATA_DIR / "da_fitly_user_activity.csv"

#Intermediate Data (Interim)
INTERIM_DATA_DIR = DATA_DIR / "interim"
INTERMEDIATE_DATA_PATH = INTERIM_DATA_DIR / "fitly_clean_data.csv"

# Output Data (Processed)
PROCESSED_DATA_DIR = DATA_DIR / "processed"
CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "fitly_clean_data.csv"


# ==========================================
# 4. BUSINESS CONSTANTS (The "Logic" part)
# ==========================================
# Use UPPER_CASE for all constants

# Column Names (prevent typos in your code)
#COL_USER_ID = "user_id"
#COL_DATE = "date"
#COL_STATUS = "subscription_status"

# Business Rules
#STATUS_ACTIVE = "Active"
#STATUS_CHURNED = "Churned"
#MIN_AGE_THRESHOLD = 18
