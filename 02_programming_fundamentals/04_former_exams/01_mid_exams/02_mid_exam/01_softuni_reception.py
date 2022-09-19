first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
students_requests = int(input())

capacity_for_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity
counter_hours = 0

while students_requests > 0:
    counter_hours += 1
    if counter_hours % 4 == 0:
        continue
    else:
        students_requests -= capacity_for_hour

print(f"Time needed: {counter_hours}h.")
