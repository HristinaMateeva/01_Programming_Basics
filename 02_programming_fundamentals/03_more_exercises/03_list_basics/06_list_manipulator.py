def exchange_category(main_list_f):
    is_valid_index = True
    exchange_index = int(category[1])
    if exchange_index >= len(main_list_f) or exchange_index < 0:
        is_valid_index = False
        return is_valid_index
    else:
        left_side = main_list_f[:exchange_index + 1]
        right_side = main_list_f[exchange_index + 1:]
        main_list_f = right_side + left_side
        return main_list_f


def max_or_min_category(even_or_odd_list_f, even_or_odd_f):
    if not even_or_odd_list_f:
        return "No matches"
    if even_or_odd_f == "max":
        element_f = max(even_or_odd_list_f)
    else:
        element_f = min(even_or_odd_list_f)
    counter_index_f = main_list.count(element_f)
    if counter_index_f == 1:
        index_f = main_list.index(element_f)
        return index_f
    else:
        for latest_index in range(len(main_list) - 1, -1, -1):
            if main_list[latest_index] == element_f:
                return latest_index


def first_or_last_category(even_or_odd_list_f, first_or_last_f):
    count_list = []
    count = int(category[1])
    if count > len(main_list):
        return "Invalid count"
    else:
        if first_or_last_f == "first":
            count_list = even_or_odd_list_f[:count]
        elif first_or_last_f == "last":
            count_list = even_or_odd_list_f[-count:]
        return count_list


main_list = [int(el) for el in input().split()]
command = input()

even_numbers_list = [element for element in main_list if element % 2 == 0]
odd_numbers_list = [element for element in main_list if element % 2 == 1]

while not command == "end":
    category = command.split()
    type_of_category = category[0]
    if type_of_category == "exchange":
        if not exchange_category(main_list):
            print("Invalid index")
        else:
            main_list = exchange_category(main_list)
        even_numbers_list = [even_el for even_el in main_list if even_el % 2 == 0]
        odd_numbers_list = [odd_el for odd_el in main_list if odd_el % 2 == 1]
    elif "even" in category:
        if type_of_category == "max":
            print(max_or_min_category(even_numbers_list, type_of_category))
        elif type_of_category == "min":
            print(max_or_min_category(even_numbers_list, type_of_category))
        elif type_of_category == "first":
            print(first_or_last_category(even_numbers_list, type_of_category))
        elif type_of_category == "last":
            print(first_or_last_category(even_numbers_list, type_of_category))
    elif "odd" in category:
        if type_of_category == "max":
            print(max_or_min_category(odd_numbers_list, type_of_category))
        elif type_of_category == "min":
            print(max_or_min_category(odd_numbers_list, type_of_category))
        elif type_of_category == "first":
            print(first_or_last_category(odd_numbers_list, type_of_category))
        elif type_of_category == "last":
            print(first_or_last_category(odd_numbers_list, type_of_category))
    command = input()

print(main_list)
