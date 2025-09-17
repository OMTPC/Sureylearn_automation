


import re
import os
import logging

logger = logging.getLogger(__name__)


# Define base data folder (where Excel files live)
DATA_DIR = "./data"


#M Map year numbers to their respective Excel file paths
YEAR_TO_FILE = {
    "1": "year1.xlsx",
    "2": "year2.xlsx",
    "3": "year3.xlsx"   
}


def get_excel_path(course_name: str) -> str:
    """
    Given a course offering name, returns the correct Excel path.
    """
    logging.debug(f"course_name = {course_name}")
    
    # Look for year number before '('
    match = re.search(r'([1-3])\s*\(', course_name)
    if match:
        year = match.group(1)
        logger.debug(f"Matched year: {year}")
        filename = YEAR_TO_FILE.get(year)
        if filename:
            path = os.path.join(DATA_DIR, filename)
            logger.debug(f"Resolved path: {path}")
            return path
        
    logger.warning(f"No matching year found in course name: {course_name}")
    return None

            