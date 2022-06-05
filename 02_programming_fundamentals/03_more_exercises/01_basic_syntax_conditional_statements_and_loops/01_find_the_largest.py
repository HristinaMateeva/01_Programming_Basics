number_as_string = input()

number_list = [int(el) for el in number_as_string]
number_list.sort(reverse=True)
number_list_as_strings = [str(el) for el in number_list]
result = ""

for el in number_list_as_strings:
    result = "".join(number_list_as_strings)

print(int(result))
