command = input()

courses = {}

while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name in courses:
        courses[course_name] += [student_name]
    else:
        courses[course_name] = [student_name]

    command = input()

for course, students_list in courses.items():
    print(f"{course}: {len(students_list)}")
    for el in students_list:
        print(f"-- {el}")
