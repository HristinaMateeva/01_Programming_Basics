from math import prod


def factorial_division(number_1, number_2):
    divisors_1 = []
    divisors_2 = []
    for num_1 in range(1, number_1 + 1):
        divisors_1.append(num_1)
    for num_2 in range(1, number_2 + 1):
        divisors_2.append(num_2)
    result = prod(divisors_1) / prod(divisors_2)
    return f"{result:.2f}"


first_num = int(input())
second_num = int(input())

print(factorial_division(first_num, second_num))
