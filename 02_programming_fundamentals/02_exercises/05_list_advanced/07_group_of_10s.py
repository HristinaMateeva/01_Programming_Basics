import math

numbers_list = input().split(", ")

numbers_list = [int(num) for num in numbers_list]
max_group = math.ceil(max(numbers_list) / 10) * 10
result = []

for number in range(10, max_group + 1, 10):
    for element in numbers_list:
        if (number - 10) < element <= number:
            result.append(element)
    print(f"Group of {number}'s: {result}")

    result = []
