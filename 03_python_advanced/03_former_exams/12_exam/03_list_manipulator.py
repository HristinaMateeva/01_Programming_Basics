def list_manipulator(sequence_numbers, command, *args):
    position = args[0]
    result = []

    if command == "add" and position == "beginning":
        numbers = args[1:]
        result.extend(numbers)
        result.extend(sequence_numbers)

    elif command == "add" and position == "end":
        numbers = args[1:]
        result.extend(sequence_numbers)
        result.extend(numbers)

    elif command == "remove" and position == "beginning":
        if len(args) == 1:
            result = sequence_numbers[1:]
        else:
            nums_to_remove = args[1]
            result = sequence_numbers[nums_to_remove:]

    elif command == "remove" and position == "end":
        if len(args) == 1:
            result = sequence_numbers[:-1]
        else:
            nums_to_remove = args[1]
            result = sequence_numbers[:nums_to_remove - 1]

    return result


# ------------------------------
print(list_manipulator([1, 2, 3], "remove", "end"))
# ------------------------------
print(list_manipulator([1, 2, 3], "remove", "beginning"))
# ------------------------------
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# ------------------------------
print(list_manipulator([1, 2, 3], "add", "end", 30))
# ------------------------------
print(list_manipulator([1, 2, 3], "remove", "end", 2))
# ------------------------------
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# ------------------------------
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# ------------------------------
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
# ------------------------------
