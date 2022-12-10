from collections import deque

type_bombs = {"Datura": 40, "Cherry": 60, "Smoke Decoy": 120}
created_bombs = {"Datura": 0, "Cherry": 0, "Smoke Decoy": 0}
needed_bombs_created = False

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    current_sum = current_effect + current_casing

    if current_sum == type_bombs["Datura"]:
        created_bombs["Datura"] += 1
    elif current_sum == type_bombs["Cherry"]:
        created_bombs["Cherry"] += 1
    elif current_sum == type_bombs["Smoke Decoy"]:
        created_bombs["Smoke Decoy"] += 1
    else:
        current_casing -= 5
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing)

    if created_bombs["Datura"] >= 3 and created_bombs["Cherry"] >= 3 and created_bombs["Smoke Decoy"] >= 3:
        needed_bombs_created = True
        break

if needed_bombs_created:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
else:
    print("Bomb Casings: empty")

sorted_bombs = dict(sorted(created_bombs.items(), key=lambda x: x[0]))

for type_bomb, value in sorted_bombs.items():
    print(f"{type_bomb} Bombs: {value}")
