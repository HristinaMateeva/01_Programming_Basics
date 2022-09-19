numbers = [int(el) for el in input().split()]

total = 0
result = []

for element in numbers:
    total += element

average = total / len(numbers)

for num in numbers:
    if num > average:
        result.append(num)

result.sort(reverse=True)
if len(result) > 5:
    result = result[:5]
result = [str(n) for n in result]

if not result:
    print("No")
else:
    print(" ".join(result))
