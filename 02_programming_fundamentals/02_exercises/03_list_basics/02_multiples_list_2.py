factor = int(input())
count = int(input())

result_list = []

for i in range(factor, factor * count + 1, factor):
    result_list.append(i)

print(result_list)
