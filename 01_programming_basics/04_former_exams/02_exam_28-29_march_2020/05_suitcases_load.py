capacity = float(input())
command = input()

counter = 0
available_space = capacity
is_cargo_full = False
total_loaded = 0

while command != "End":
    volume = float(command)
    counter += 1
    if counter % 3 == 0:
        volume *= 1.10
    available_space -= volume
    total_loaded += volume
    if capacity < total_loaded:
        is_cargo_full = True
        counter -= 1
        break

    command = input()

if is_cargo_full:
    print(f"No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")
