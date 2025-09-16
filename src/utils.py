


import re
from src.config import year_MAPPING


def get_year_from_course(course_name: str) -> str:
    """
    Extract year from course name using year_MAPPING keys.
    Returns the corresponding year path or None if not found.
    """

    print(f"DEBUG: course_name = {course_name}")


    match = re.search(r"\b([1-3])\s*\(", course_name)
    if match:
        print(f"DEBUG: matched pattern '([1-3])\\s*(': {match.group(1)}")
        return match.group(1)

    match = re.search(r"\b([1-3])\b", course_name)
    if match:
        print(f"DEBUG: matched pattern '([1-3])': {match.group(1)}")
        return match.group(1)
    
    print("DEBUG: no match found")
    return None
    

def get_excsl_path(course_name: str) -> str:
    """
    Given a course offering name, returns the correct Excel path.
    """
    year = get_year_from_course(course_name)
    if year and year in year_MAPPING:
        return year_MAPPING[year]
    return None

