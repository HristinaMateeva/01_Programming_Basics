command = input()

courses_data = {}

while not command == "end":
    course, name = command.split(" : ")
    if course not in courses_data:
        courses_data[course] = [name]
    else:
        courses_data[course].append(name)
    command = input()

for type_course, students in courses_data.items():
    print(f"{type_course}: {len(courses_data[type_course])}")
    for student in students:
        print(f"-- {student}")
