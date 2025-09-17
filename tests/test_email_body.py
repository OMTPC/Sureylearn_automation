

from src.parser import parse_email_text

# example email body
email_body = """
Assignment Submission Complete:

*       Submission ID: 3074832
*       Course Offering Code: NUR2189_2025-6_XAY_XS9
*       Course Offering Name: MENTAL HEALTH NURSING 2 (NUR2189) - XAY 2025/6
*       Assignment: Infection, Prevention and Control
*       User: GABRIELLA AUSTIN
"""

parsed = parse_email_text(email_body)
print("Parsed result:", parsed)
