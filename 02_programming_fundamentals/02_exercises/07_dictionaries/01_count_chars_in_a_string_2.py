data = input().split()

current_dict = {}
result = {}

for elements in data:
    current_dict = {}
    for letter in elements:
        current_dict[letter] = elements.count(letter)
    if not result:
        result.update(current_dict)
    else:
        for key, value in current_dict.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value

for char, occurrences in result.items():
    print(f"{char} -> {occurrences}")
