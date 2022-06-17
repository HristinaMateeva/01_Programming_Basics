n = int(input())

even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []

for iteration in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even_nums.append(current_number)
    if not current_number % 2 == 0:
        odd_nums.append(current_number)
    if current_number < 0:
        negative_nums.append(current_number)
    if current_number >= 0:
        positive_nums.append(current_number)

command = input()
if command == "positive":
    print(positive_nums)
elif command == "negative":
    print(negative_nums)
elif command == "even":
    print(even_nums)
if command == "odd":  # else:
    print(odd_nums)
