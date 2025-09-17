


import logging
from src.parser import parse_email_text as parse_email

logging.basicConfig(level=logging.INFO)

def test_parser():
    sample_email = """Assignment Submission Complete:
    Submission ID: 3074514
    Course Offering Code: NUR3328_2025-6_XAY_XS9
    Course Offering Name: MENTAL HEALTH NURSING 3 (NUR3328) - XAY 2025/6
    Assignment: Infection Prevention and Control
    User: ISABEL TURNER"""

    logging.info("Running parser test with sample email")
    parsed = parse_email(sample_email)
    print(parsed)


if __name__ == "__main__":
    test_parser()

