input_line = input()

name_and_id = {}
name_and_course = {}

while ":" in input_line:
    student_name, student_id, course = input_line.split(":")
    name_and_id[student_name] = student_id
    name_and_course[student_name] = course

    input_line = input()

exact_course = " ".join(input_line.split("_"))

for key, value in name_and_course.items():
    if value == exact_course:
        print(f"{key} - {name_and_id.get(key)}")
