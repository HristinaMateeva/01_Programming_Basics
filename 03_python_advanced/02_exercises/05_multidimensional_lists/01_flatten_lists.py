input_line = input().split("|")

result = []

for index in range(len(input_line) - 1, -1, -1):
    sub_list = input_line[index].split()
    result.extend(sub_list)

print(*result)
