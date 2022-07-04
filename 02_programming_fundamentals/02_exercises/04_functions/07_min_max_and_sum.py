def min_and_max_sum(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_of_nums = sum(nums)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_of_nums}")


numbers = input().split()
numbers = [int(el) for el in numbers]

min_and_max_sum(numbers)
