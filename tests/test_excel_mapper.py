

from src.excel_mapper import get_excel_path as map_course_to_excel

def test_excel_mapper():
    course_names = [
        "MENTAL HEALTH NURSING 1 (NUR1123) - XAY 2025/6",
        "MENTAL HEALTH NURSING 2 (NUR2224) - XAY 2025/6",
        "MENTAL HEALTH NURSING 3 (NUR3328) - XAY 2025/6",
    ]

    for name in course_names:
        path = map_course_to_excel(name)
        print(f"{name} -> {path}")


if __name__ == "__main__":
    test_excel_mapper()
