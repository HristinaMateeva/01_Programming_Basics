numbers_list = input().split(", ")

number_list_int = [int(num) for num in numbers_list]

positive_numbers_int = [num for num in number_list_int if num >= 0]
negative_numbers_int = [num for num in number_list_int if num < 0]
even_numbers_int = [num for num in number_list_int if num % 2 == 0]
odd_numbers_int = [num for num in number_list_int if num % 2 == 1]

positive_numbers_str = [str(num) for num in positive_numbers_int]
negative_numbers_str = [str(num) for num in negative_numbers_int]
even_numbers_str = [str(num) for num in even_numbers_int]
odd_numbers_str = [str(num) for num in odd_numbers_int]

print(f"Positive: {', '.join(positive_numbers_str)}")
print(f"Negative: {', '.join(negative_numbers_str)}")
print(f"Even: {', '.join(even_numbers_str)}")
print(f"Odd: {', '.join(odd_numbers_str)}")

