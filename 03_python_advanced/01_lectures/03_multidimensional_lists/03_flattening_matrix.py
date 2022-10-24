rows = int(input())

result = []

for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    result.extend(nums)

print(result)
