num_list = input().split(", ")
num_beggars = int(input())

result_list = []
current_beggar_result = 0

if num_beggars == len(num_list):
    for item in num_list:
        item = int(item)
        result_list.append(item)
    print(result_list)

elif num_beggars < len(num_list):
    for item_1 in num_list:
        item_1 = int(item_1)
        # current_beggar_result = 0
        for num in range(1, len(num_list), num_beggars):
            current_beggar_result += item_1
    result_list.append(current_beggar_result)

    print(result_list)

elif num_beggars > len(num_list):
    for item_2 in num_list:
        item_2 = int(item_2)

#Не е довършена