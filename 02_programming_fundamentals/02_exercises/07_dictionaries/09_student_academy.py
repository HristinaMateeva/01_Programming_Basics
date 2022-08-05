number = int(input())

students_data = {}
average_grades = {}

for num in range(number):
    name = input()
    grade = float(input())
    if name not in students_data:
        students_data[name] = [grade]
    else:
        students_data[name].append(grade)

for student in students_data:
    average_grade = sum(students_data[student]) / len(students_data[student])
    if average_grade >= 4.50:
        average_grades[student] = average_grade

for student_name, av_grade in average_grades.items():
    print(f"{student_name} -> {av_grade:.2f}")
