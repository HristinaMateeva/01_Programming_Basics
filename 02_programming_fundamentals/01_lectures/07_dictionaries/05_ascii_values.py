characters = input().split(", ")

result_dict = {}

for character in characters:
    result_dict[character] = ord(character)

print(result_dict)
