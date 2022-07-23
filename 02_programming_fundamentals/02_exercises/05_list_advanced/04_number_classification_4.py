numbers_list = input().split(", ")

number_list_int = [int(num) for num in numbers_list]

positive_numbers = [str(num) for num in number_list_int if num >= 0]
negative_numbers = [str(num) for num in number_list_int if num < 0]
even_numbers = [str(num) for num in number_list_int if num % 2 == 0]
odd_numbers = [str(num) for num in number_list_int if num % 2 == 1]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
