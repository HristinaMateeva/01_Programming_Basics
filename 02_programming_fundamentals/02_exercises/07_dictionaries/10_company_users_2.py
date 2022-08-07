command = input()

data = {}
is_id_in_data = False

while not command == "End":
    company_name, employee_id = command.split(" -> ")
    if company_name in data and employee_id not in data[company_name]:
        data[company_name] += [employee_id]
    elif company_name not in data:
        data[company_name] = [employee_id]

    command = input()

for company, emp_id in data.items():
    print(f"{company}")
    for el in emp_id:
        print(f"-- {el}")
