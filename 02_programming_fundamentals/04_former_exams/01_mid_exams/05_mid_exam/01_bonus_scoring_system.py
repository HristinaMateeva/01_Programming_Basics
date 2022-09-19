from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for student in range(1, students + 1):
    current_student_attendance = int(input())
    total_bonus = current_student_attendance / lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = current_student_attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
