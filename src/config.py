

import os
from dotenv import load_dotenv


# Load .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))


# Email Credentials
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# IMAP settings (default for Office 365)
IMAP_SERVER = os.getenv("IMAP_SERVER", "outlook.office365.com")
IMAP_PORT = int(os.getenv("IMAP_PORT", 993))    
MAIL_FOLDER = os.getenv("MAIL_FOLDER", "INBOX")


# Excel settings
EXCEL_PATH = os.getenv("EXCEL_PATH", "data/mandatory_training.xlsx")

# Dry run toggle
DRY_RUN = os.getenv("DRY_RUN", "True").lower() in ("1", "true", "yes")