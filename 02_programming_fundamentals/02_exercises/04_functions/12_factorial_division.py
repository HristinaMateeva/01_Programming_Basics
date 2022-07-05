def factorial_division(number_1, number_2):
    factorial_1 = 1
    factorial_2 = 1
    for num_1 in range(1, number_1 + 1):
        factorial_1 *= num_1
    for num_2 in range(1, number_2 + 1):
        factorial_2 *= num_2
    result = factorial_1 / factorial_2
    return f"{result:.2f}"


first_num = int(input())
second_num = int(input())

print(factorial_division(first_num, second_num))
