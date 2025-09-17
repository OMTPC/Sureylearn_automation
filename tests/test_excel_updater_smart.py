


from src.excel_updater import update_excel_with_submission 

sample_email = {
    "submission_id": "3074515",
    "course_code": "NUR3328_2025-6_XAY_XS9",
    "course_name": "MENTAL HEALTH NURSING 3 (NUR3328) - XAY 2025/6",
    "assignment": "basic life support",
    "user": "alberto rui"
}

if __name__ == "__main__":
    result = update_excel_with_submission(sample_email)
    print("Update result:", result)

    