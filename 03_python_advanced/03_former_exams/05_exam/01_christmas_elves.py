from collections import deque

elves_energy = deque([int(el) for el in input().split()])
material_boxes = [int(el) for el in input().split()]

toys = 0
counter = 0
made_toys = 0
total_used_energy = 0

while elves_energy and material_boxes:
    current_energy = elves_energy.popleft()
    if current_energy < 5:
        continue

    counter += 1
    current_box = material_boxes.pop()
    if counter % 3 == 0 and current_energy >= (current_box * 2):
        made_toys = 2
        total_used_energy += (current_box * 2)
        current_energy -= (current_box * 2) - 1
        if counter % 5 == 0:
            made_toys = 0
            current_energy -= 1
    elif current_energy >= current_box and not counter % 3 == 0:
        made_toys = 1
        total_used_energy += current_box
        current_energy -= (current_box - 1)
        if counter % 5 == 0:
            made_toys = 0
            current_energy -= 1
    else:
        material_boxes.append(current_box)
        current_energy *= 2

    elves_energy.append(current_energy)
    toys += made_toys
    made_toys = 0

print(f"Toys: {toys}")
print(f"Energy: {total_used_energy}")
if elves_energy:
    print(f"Elves left: {', '.join([str(el) for el in elves_energy])}")
if material_boxes:
    print(f"Boxes left: {', '.join([str(el) for el in material_boxes])}")
