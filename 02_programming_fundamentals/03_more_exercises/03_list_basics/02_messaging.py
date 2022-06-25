sequence_of_numbers = input().split()
string = input()

string_as_list = [x for x in string]  #Coverting the string into list
message = []

for symbol in sequence_of_numbers:
    nums_for_searched_index = [int(x) for x in symbol]
    current_index = sum(nums_for_searched_index)
    if len(string_as_list) <= current_index:
        index = current_index - len(string_as_list)
    else:
        index = current_index
    message.append(string_as_list[index])
    string_as_list.pop(index)

print("".join(message))
