


import logging
from src.parser import parse_surreylearn_email
from src.email_connector import fetch_surreylearn_emails

# logging.basicConfig(level=logging.INFO)

# def test_parser():
#     sample_email = """Assignment Submission Complete:
#     Submission ID: 3074514
#     Course Offering Code: NUR3328_2025-6_XAY_XS9
#     Course Offering Name: MENTAL HEALTH NURSING 3 (NUR3328) - XAY 2025/6
#     Assignment: Infection Prevention and Control
#     User: ISABEL TURNER"""

#     logging.info("Running parser test with sample email")
#     parsed = parse_email(sample_email)
#     print(parsed)



if __name__ == "__main__":
    emails = fetch_surreylearn_emails(limit=10)  # just first 10 emails
    print(f"Found {len(emails)} SurreyLearn emails.\n")

    for i, msg in enumerate(emails, start=1):
        parsed = parse_surreylearn_email(msg)
        if parsed:
            print(f"{i}. {parsed['user']} | {parsed['assignment']} | {parsed['course_name']}")
        else:
            print(f"{i}. ⚠️ Could not parse email")
