numbers = [int(el) for el in input().split()]
command = input()

counter_shots = 0

while not command == "End":
    target_index = int(command)
    if target_index < 0 or target_index >= len(numbers) or numbers[target_index] == -1:
        command = input()
        continue
    target = numbers[target_index]
    counter_shots += 1
    numbers[target_index] = -1
    for index in range(len(numbers)):
        if numbers[index] > target and numbers[index] != -1:
            numbers[index] -= target
        elif numbers[index] <= target and numbers[index] != -1:
            numbers[index] += target
    command = input()

numbers = [str(num) for num in numbers]
print(f"Shot targets: {counter_shots} -> {' '.join(numbers)}")
