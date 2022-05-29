num_students = int(input())
total_students = 0
grade_total = 0
students_2_to_3 = 0
students_3_to_4 = 0
students_4_to_5 = 0
top_students = 0

for num in range(1, num_students+ 1):
    grade = float(input())
    if 2 <= grade < 3:
        students_2_to_3 += 1
        grade_total += grade
    elif 3 <= grade < 4:
        students_3_to_4 += 1
        grade_total += grade
    elif 4 <= grade < 5:
        students_4_to_5 += 1
        grade_total += grade
    elif grade >= 5:
        top_students += 1
        grade_total += grade

total_students = students_2_to_3 + students_3_to_4 + students_4_to_5 + top_students
average_grades = grade_total / total_students
percent_top_students = top_students / total_students * 100
percent_students_2_to_3 = students_2_to_3 / total_students * 100
percent_students_3_to_4 = students_3_to_4 / total_students * 100
percent_students_4_to_5 = students_4_to_5 / total_students * 100

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_students_4_to_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_students_3_to_4:.2f}%")
print(f"Fail: {percent_students_2_to_3:.2f}%")
print(f"Average: {average_grades:.2f}")
