import math
needed_hours = int(input())
days = int(input())
num_employees_overtime = int(input())

working_hours = (8 * days) * 0.9
overtime = num_employees_overtime * 2 * days
total_working_hours = working_hours + overtime
difference = abs(total_working_hours - needed_hours)

if total_working_hours >= needed_hours:
    print(f"Yes!{math.floor(difference)} hours left.")
elif total_working_hours < needed_hours:
    print(f"Not enough time!{math.ceil(difference)} hours needed.")
