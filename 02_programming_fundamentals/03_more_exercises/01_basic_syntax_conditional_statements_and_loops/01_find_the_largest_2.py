number_as_string = input()

result_list = []
result_string = ""
result_num = 0

for item in number_as_string:
    result_list.append(item)  #Converting the string into list

result_list.sort(reverse=True)  #Reverse the list in descending order

for item_1 in result_list:
    result_string = "".join(result_list)  #Coverting the list back to string

print(int(result_num))
