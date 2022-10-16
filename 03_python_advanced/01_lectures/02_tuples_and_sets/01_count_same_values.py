nums = (float(el) for el in input().split())
occurrences = {}

for num in nums:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for key, value in occurrences.items():
    print(f"{key} - {value} times")
