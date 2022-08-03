resource = input()

result = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in result:
        result[resource] = quantity
    else:
        result[resource] += quantity
    resource = input()

for key, value in result.items():
    print(f"{key} -> {value}")
