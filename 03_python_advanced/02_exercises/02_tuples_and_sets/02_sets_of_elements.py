m, n = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for _ in range(m):
    first_set.add(int(input()))

for _ in range(n):
    second_set.add(int(input()))

common_nums = first_set.intersection(second_set)

for num in common_nums:
    print(num)
