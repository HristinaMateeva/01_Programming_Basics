num_lines = int(input())

for num in range(num_lines):
    sentence = input()
    first_index_name = 0
    last_index_name = 0
    first_index_age = 0
    last_index_age = 0

    for index, char in enumerate(sentence):
        if char == "@":
            first_index_name = index + 1
        elif char == "|":
            last_index_name = index - 1
        elif char == "#":
            first_index_age = index + 1
        elif char == "*":
            last_index_age = index - 1

    name = sentence[first_index_name: (last_index_name + 1):]
    age = sentence[first_index_age: last_index_age + 1: ]
    print(f"{name} is {age} years old.")
