def is_index_in_range(nums, f_index):
    if 0 <= f_index < len(nums):
        return True
    return False


def shoot(nums, f_index, f_value):
    if is_index_in_range(nums, f_index):
        nums[f_index] -= f_value
        if nums[f_index] <= 0:
            nums.pop(f_index)
    return nums


def add_target(nums, f_index, f_value):
    if is_index_in_range(nums, f_index):
        nums.insert(f_index, f_value)
    else:
        print("Invalid placement!")
    return nums


def strike(nums, f_index, f_value):
    left_index = f_index - f_value
    right_index = f_index + f_value

    if left_index >= 0 and right_index < len(nums):
        left_part = nums[:left_index]
        right_part = nums[right_index + 1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums


targets = [int(target) for target in input().split()]
data = input()

while not data == "End":
    command, index, value = data.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add_target(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)

    data = input()

print("|".join([str(el) for el in targets]))
