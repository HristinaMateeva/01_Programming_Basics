from collections import deque

fireworks_effect = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]

total_fireworks = {"Palm": 0, "Willow": 0, "Crossette": 0}
enough_fireworks = False

while fireworks_effect and explosive_power:
    current_effect = fireworks_effect.popleft()
    current_explosive = explosive_power.pop()

    if current_effect <= 0:
        explosive_power.append(current_explosive)
        continue
    if current_explosive <= 0:
        fireworks_effect.appendleft(current_effect)
        continue
    current_sum = current_effect + current_explosive

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        total_fireworks["Crossette"] += 1
    elif current_sum % 3 == 0:
        total_fireworks["Palm"] += 1
    elif current_sum % 5 == 0:
        total_fireworks["Willow"] += 1
    else:
        current_effect -= 1
        fireworks_effect.append(current_effect)
        explosive_power.append(current_explosive)

    if total_fireworks["Palm"] >= 3 and total_fireworks["Willow"] >= 3 and total_fireworks["Crossette"] >= 3:
        enough_fireworks = True
        break

if enough_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join([str(el) for el in fireworks_effect])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

for firework, quantity in total_fireworks.items():
    print(f"{firework} Fireworks: {quantity}")
