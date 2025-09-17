from src.email_connector import fetch_surreylearn_emails
from src.parser import parse_surreylearn_email
from pprint import pprint

def test_real_emails():
    # Fetch unread SurreyLearn emails
    emails = fetch_surreylearn_emails()
    print(f"Found {len(emails)} unread SurreyLearn emails.\n")

    if not emails:
        print("No unread emails found. Exiting test.")
        return

    # Limit to first 10 emails for testing
    for i, msg in enumerate(emails[:10], start=1):
        # msg is a COM MailItem
        parsed = parse_surreylearn_email(msg)
        
        print(f"Email {i}:")
        if parsed:
            pprint(parsed)
        else:
            print("⚠️ Could not parse email")

if __name__ == "__main__":
    test_real_emails()
