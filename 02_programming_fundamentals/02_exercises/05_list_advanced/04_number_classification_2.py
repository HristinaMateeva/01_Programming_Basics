def positive_numbers(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if int(number) < 0]


def even_numbers(numbers):
    return [number for number in numbers_as_string if int(number) % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers_as_string if int(number) % 2 != 0]


numbers_as_string = input().split(", ")
print(f"Positive: {', '.join(positive_numbers(numbers_as_string))}")
print(f"Negative: {', '.join(negative_numbers(numbers_as_string))}")
print(f"Even: {', '.join(even_numbers(numbers_as_string))}")
print(f"Odd: {', '.join(odd_numbers(numbers_as_string))}")
