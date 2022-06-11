num_lines = int(input())

total_sum = 0

for num in range(num_lines):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")
