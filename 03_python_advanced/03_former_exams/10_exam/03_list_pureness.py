from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    k_num = args[1]
    best_pureness = 0
    best_rotation = 0

    for rotation in range(k_num + 1):
        current_pureness = 0

        for index, value in enumerate(numbers):
            current_pureness += index * value

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation

        numbers.rotate(1)
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


# ------------------------------
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
# ------------------------------
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
# ------------------------------
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
