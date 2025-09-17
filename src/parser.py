
"""
src/parser.py

Parse SurreyLearn "Assignment Submission Complete" emails and return a dict
with keys like:
  - submission_id
  - course_code
  - course_name
  - assignment
  - user (student full name, title-cased)
  - student_email (if present)
"""

import re
import logging
from pprint import pprint

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

EMAIL_RE = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")

# Label patterns (flexible, case-insensitive, tolerate spaces around label and colon)
PATTERNS = {
    'submission_id': re.compile(r'(?mi)submission\s*id\s*[:\-]\s*(.+)'),
    'course_code': re.compile(r'(?mi)course\s*offering\s*code\s*[:\-]\s*(.+)'),
    'course_name': re.compile(r'(?mi)course\s*offering\s*name\s*[:\-]\s*(.+)'),
    'assignment': re.compile(r'(?mi)^assignment\s*[:\-]\s*(.+)', re.MULTILINE),
    'user': re.compile(r'(?mi)^(?:user|student)\s*[:\-]\s*(.+)', re.MULTILINE),
}


def _normalise_name(name: str) -> str:
    """
    Normalise a user's name:
    - Strip leading/trailing spaces
    - Collapse multiple spaces into one
    - Convert to title case (each word capitalised)
    """
    if not name:
        return ""

    # Strip whitespace and split on spaces
    parts = name.strip().split()
    # Join back with a single space
    cleaned = " ".join(parts)
    # Return in Title Case (e.g., 'john smith' -> 'John Smith')
    return cleaned.title()



def parse_email_text(text: str) -> dict:
    """
    Parse the email body text and return a dictionary with extracted fields.
    Uses labelled regex patterns first, then a generic 'key: value' line scanner as fallback.
    """
    if not text:
        return {}
    

    parsed = {}
    # first pass: labelled regex patterns

    for key, pat in PATTERNS.items():
        match = pat.search(text)
        if match:
            parsed[key] = match.group(1).strip()

    # find an email address anywhere in the text if present
    m_email = EMAIL_RE.search(text)
    if m_email:
        parsed['student_email'] = m_email.group(0).lower()

    
    # fallback: scan lines "Label: value" to capture anything missed
    if not all(k in parsed for k in ('submission_id', 'course_code', 'course_name', 'assignment', 'user')):
        for line in text.splitlines():
            if ':' not in line:
                continue
            left, right = map(str.strip, line.split(':', 1))
            key_norm = left.lower()
            if key_norm in ('submission id', 'submissionid'):
                parsed.setdefault('submission_id', right)
            elif key_norm in ('course offering code', 'course code'):
                parsed.setdefault('course_code', right)
            elif key_norm in ('course offering name', 'course name'):
                parsed.setdefault('course_name', right)
            elif key_norm == 'assignment':
                parsed.setdefault('assignment', right)
            elif key_norm in ('user', 'student'):
                parsed.setdefault('user', right)
            # check for email-like token in the right-hand side
            m = EMAIL_RE.search(right)
            if m and 'student_email' not in parsed:
                parsed['student_email'] = m.group(0).lower()

    
    # normalise user name
    if 'user' in parsed:
        parsed['user'] = _normalise_name(parsed['user']) 

    
    # final cleanup: strip any surrounding quotes from values
    for k, v in list(parsed.items()):
        if isinstance(v, str):
            parsed[k] = v.strip()

    
    return parsed


if __name__ == "__main__":
    SAMPLE = """Assignment Submission Complete:
            Submission ID: 3074514
            Course Offering Code: NUR3328_2025-6_XAY_XS9
            Course Offering Name: MENTAL HEALTH NURSING 3 (NUR3328) - XAY 2025/6
            Assignment: Infection Prevention and Control
            User: ISABEL TURNER
            """
    logging.info("Running parser test with sample email")
    result = parse_email_text(SAMPLE)
    pprint(result)


