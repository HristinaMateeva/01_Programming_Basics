words = input().split()

result = {}

for word in words:
    char_list = []
    for char in word:
        char_list.append(char)

    for el in char_list:
        if el not in result:
            result[el] = 1
        else:
            result[el] += 1

for key, value in result.items():
    print(f"{key} -> {value}")
