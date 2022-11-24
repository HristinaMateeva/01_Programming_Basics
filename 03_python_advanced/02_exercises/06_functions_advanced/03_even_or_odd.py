def even_odd(*args):
    nums = [int(el) for el in args[:-1]]
    command = args[-1]
    if command == "odd":
        odd_nums = [el for el in nums if el % 2 == 1]
        return odd_nums
    elif command == "even":
        even_nums = [el for el in nums if el % 2 == 0]
        return even_nums


# ------------------------------
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# ------------------------------
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
