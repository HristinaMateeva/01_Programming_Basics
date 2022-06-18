single_string = input()

changed_string = single_string.split()
final_list = []

for element in changed_string:
    converted_number = int(element) * -1
    final_list.append(converted_number)

print(final_list)
