

# main.py
from src.email_connector import fetch_surreylearn_emails
from src.parser import parse_surreylearn_email
from src.excel_updater import update_excel_with_submission

def fetch_and_preview_emails(limit=10):
    """Fetch unread SurreyLearn emails and print a preview."""
    emails = fetch_surreylearn_emails(limit=limit)
    print(f"Found {len(emails)} unread SurreyLearn emails.\n")

    # preview email subjects and sender names
    for i, email in enumerate(emails, start=1):
        print(f"Email {i}: Sender='{email.SenderName}', Subject='{email.Subject}'")

    return emails

def fetch_and_parse_emails(limit=10):
    """Fetch emails and parse them into dictionaries."""
    emails = fetch_surreylearn_emails(limit=limit)
    print(f"Found {len(emails)} unread SurreyLearn emails.\n")

    parsed_emails = []

    for i, email in enumerate(emails, start=1):
        parsed = parse_surreylearn_email(email)
        if parsed:
            parsed_emails.append(parsed)
            print(f"Email {i} parsed: {parsed['user']} - {parsed['assignment']}")
        else:
            print(f"Email {i}: ⚠️ Could not parse")

    return parsed_emails


def process_parsed_emails(parsed_emails):
    """Update Excel files with parsed email submissions."""
    for parsed in parsed_emails:
        success = update_excel_with_submission(parsed)
        if success:
            print(f"{parsed['user']} - {parsed['assignment']} → Excel updated ✅")
        else:
            print(f"{parsed['user']} - {parsed['assignment']} → ⚠️ Excel update failed")






if __name__ == "__main__":
    parsed_emails = fetch_and_parse_emails(limit=10)
    process_parsed_emails(parsed_emails)