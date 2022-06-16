number = int(input())
word = input()

full_list = []
filtered_list = []

for index in range(number):
    current_string = input()
    full_list.append(current_string)
    if word in full_list[index]:
        filtered_list.append(full_list[index])

print(full_list)
print(filtered_list)
