

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
year1_PATH = "./data/year1.xlsx"
year2_PATH = "./data/year2.xlsx"
year3_PATH = "./data/year3.xlsx"


year_MAPPING = {
    "1": year1_PATH,
    "2": year2_PATH,
    "3": year3_PATH
}


# Dry run toggle
DRY_RUN = os.getenv("DRY_RUN", "True").lower() in ("1", "true", "yes")