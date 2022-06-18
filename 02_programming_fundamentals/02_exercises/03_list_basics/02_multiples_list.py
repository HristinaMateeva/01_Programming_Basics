factor = int(input())
count = int(input())

result = []

for index in range(1, count + 1):
    current_element = factor * index
    result.append(current_element)

print(result)
