


from src.email_connector import fetch_surreylearn_emails

if __name__ == "__main__":
    emails = fetch_surreylearn_emails(limit=50)  # limit to first 50 messages for testing
    print(f"Found {len(emails)} SurreyLearn assignment emails.\n")

    for i, msg in enumerate(emails[:10], start=1):
        sender = getattr(msg, "SenderName", "<unknown>")
        subject = getattr(msg, "Subject", "<no subject>")
        print(f"{i}. From: {sender} | Subject: {subject}")
