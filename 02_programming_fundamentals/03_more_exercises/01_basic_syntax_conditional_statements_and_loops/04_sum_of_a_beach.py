input_string = input().lower()
valid_words = ["sand", "water", "fish", "sun"]

counter = 0

for el in valid_words:
    if el in input_string:
        counter += input_string.count(el)

print(counter)
