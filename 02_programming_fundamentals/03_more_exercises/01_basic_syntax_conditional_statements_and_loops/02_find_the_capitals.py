word = input()

result_list = []

for index, element in enumerate(word):
    if element.isupper():
        result_list.append(index)

print(result_list)
