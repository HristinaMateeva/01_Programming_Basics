nums = list(map(input().split(", ")))
even_nums = list(filter(lambda num: num % 2 == 0, nums))

print(even_nums)
