


from src.email_connector import fetch_surreylearn_emails
from src.excel_updater import mark_training_completed
from src.config import year1_PATH, year2_PATH, year3_PATH, year_MAPPING


# Fetch unread SurreyLearn emails
emails = fetch_surreylearn_emails()


for email in emails:
    course_offering = email["course_offering"]

    year = None
    for k, v  in year_MAPPING.items():
        if k in course_offering:
            year = v
            break
    if year is None:
        continue

    mark_treining_completed(
        student_name=email["student_name"], 
        assignment_name=email["assignment_name"],
        excel_path=year
        )
    

    # Mark email as read
    email["msg"].UnRead = False