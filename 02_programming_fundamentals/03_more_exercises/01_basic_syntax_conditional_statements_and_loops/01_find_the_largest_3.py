number_as_string = input()

result_list = []
result = ""

for item in number_as_string:
    result_list.append(item)  #Converting the string into list

result_list.sort()  #Sort the list in ascending order
result_list.reverse()  #Reverse the list in descending order

for item_1 in result_list:
    result = "".join(result_list)  #Coverting the list back to string

print(int(result))
