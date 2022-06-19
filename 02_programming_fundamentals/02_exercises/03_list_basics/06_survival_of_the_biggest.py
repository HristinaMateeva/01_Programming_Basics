input_line = input().split()
number_to_remove = int(input())

result_list = []

numbers_as_int = [int(el) for el in input_line]
numbers_as_int.sort()

for i in range(number_to_remove):
    numbers_as_int.pop(0)

for element in input_line:
    if int(element) in numbers_as_int:
        result_list.append(element)

print(", ".join(result_list))
