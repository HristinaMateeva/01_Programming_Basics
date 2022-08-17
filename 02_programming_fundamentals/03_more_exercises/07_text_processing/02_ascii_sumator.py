first_char = input()
second_char = input()
sequence_of_chars = input()

char_range = range(ord(first_char) + 1, ord(second_char))
total_sum = 0

for char in sequence_of_chars:
    if ord(char) in char_range:
        total_sum += ord(char)

print(total_sum)
