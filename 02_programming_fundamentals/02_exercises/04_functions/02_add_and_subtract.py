def sum_numbers(num_1, num_2):
    sum_nums = num_1 + num_2
    return sum_nums


def subtract(current_result, num_3):
    second_result = current_result - num_3
    return second_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

first_result = sum_numbers(first_num, second_num)
print(subtract(first_result, third_num))
