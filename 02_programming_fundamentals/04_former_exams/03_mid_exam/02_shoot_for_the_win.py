numbers = [int(el) for el in input().split()]
command = input()

counter_shots = 0
result = []

while not command == "End":
    result = []
    target_index = int(command)
    if target_index < 0 or target_index >= len(numbers) or numbers[target_index] == -1:
        command = input()
        continue
    target = numbers[target_index]
    counter_shots += 1
    numbers[target_index] = -1
    for element in numbers:
        if element == -1:
            result.append(-1)
        elif element > target:
            result.append(element - target)
        elif element <= target:
            result.append(element + target)
    numbers = result.copy()
    command = input()

result = numbers.copy()
result = [str(num) for num in result]
print(f"Shot targets: {counter_shots} -> {' '.join(result)}")
