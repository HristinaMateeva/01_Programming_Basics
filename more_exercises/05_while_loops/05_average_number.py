n = int(input())
sum = 0
counter = 0
average = 0

for num in range(1, n + 1):
    number = int(input())
    sum += number
    counter += 1
    average = sum / counter

print(f"{average:.2f}")
