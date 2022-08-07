data = input()

companies_data = {}

while not data == "End":
    company, user_id = data.split(" -> ")
    if company not in companies_data:
        companies_data[company] = [user_id]
    elif company in companies_data and user_id not in companies_data[company]:
        companies_data[company].append(user_id)
    data = input()

for key, value in companies_data.items():
    print(key)
    for users in companies_data[key]:
        print(f"-- {users}")
