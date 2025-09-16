


import openpyxl
import os


def mark_training_completed(student_name, assignment_name, excel_path):
    """
    Update Excel: create new student row or assignment column if missing
    """

    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel file not found: {excel_path}")


    wb = openpyxl.load_workbook(excel_path)
    ws = wb.active


    # Check if assignment column exists
    headers = [cell.value for cell in ws[1]]
    if assignment_name not in headers:
        ws.cell(row=1, column=len(headers)+1, value=assignment_name)
        col_index = len(headers) + 1
    else:
        col_index = headers.index(assignment_name) + 1

    
    # Check if student exists
    student_row = None
    for row in ws.iter_rows(min_row=2):
        if row[0].value == student_name:
            student_row = row[0].row
            break
    if student_row is None:
        student_row = ws.max_row + 1
        ws.cell(row=student_row, column=1, value=student_name)


    # Mark as done
    ws.cell(row=student_row, column=col_index, value="✅")
    wb.save(excel_path)