from collections import deque

milligrams_caffeine = [int(el) for el in input().split(", ")]
energy_drinks = deque([int(el) for el in input().split(", ")])

total_caffeine = 0
max_caffeine_per_day = 300

while milligrams_caffeine and energy_drinks:
    current_caffeine = milligrams_caffeine.pop()
    current_drink = energy_drinks.popleft()
    dose_caffeine = current_caffeine * current_drink

    if dose_caffeine + total_caffeine <= max_caffeine_per_day:
        total_caffeine += dose_caffeine
    else:
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0
        energy_drinks.append(current_drink)

    if total_caffeine >= 300:
        break

if energy_drinks:
    print(f"Drinks left: {', '.join(str(el) for el in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
