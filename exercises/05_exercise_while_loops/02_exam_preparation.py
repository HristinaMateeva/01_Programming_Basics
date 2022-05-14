number_poor_grades = int(input())

still_preparing = True
counter_poor_grades = 0
counter_all_grades = 0
last_problem = " "
sum_grades = 0

while counter_poor_grades < number_poor_grades:
    task_name = input()
    if task_name == "Enough":
        still_preparing = False
        break
    grade = int(input())
    if grade <= 4:
        still_preparing = True
        counter_poor_grades += 1
    sum_grades += grade
    counter_all_grades += 1
    last_problem = task_name

average = sum_grades / counter_all_grades

if not still_preparing:
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {counter_all_grades}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {counter_poor_grades} poor grades.")
