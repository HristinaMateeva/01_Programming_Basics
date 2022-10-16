nums = tuple([float(el) for el in input().split()])
occurrences = {}

for num in nums:
    occurrences[num] = nums.count(num)

for data in occurrences.items():
    print(f"{data[0]} - {data[1]} times")
