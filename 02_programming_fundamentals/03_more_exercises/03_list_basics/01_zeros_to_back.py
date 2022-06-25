line = input().split(", ")

line = [int(num) for num in line]
result = []
zero_list = []

for el in line:
    if el == 0:
        zero_list.append(el)
    else:
        result.append(el)

result.extend(zero_list)

print(result)
