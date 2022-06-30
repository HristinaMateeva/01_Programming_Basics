def calculation(operator, num_1, num_2):
    result = 0
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = num_1 / num_2
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return f"{int(result)}"


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculation(input_operator, first_num, second_num))
