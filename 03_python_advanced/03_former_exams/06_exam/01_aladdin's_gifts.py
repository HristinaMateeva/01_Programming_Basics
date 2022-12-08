from collections import deque

MAPPER = {
    "Gemstone": range(100, 200),
    "Porcelain Sculpture": range(200, 300),
    "Gold": range(300, 400),
    "Diamond Jewellery": range(400, 500)
}

presents_dict = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

materials = [int(el) for el in input().split()]
magic_levels = deque([int(el) for el in input().split()])

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    current_sum = current_material + current_magic_level

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_material *= 2
            current_magic_level *= 3
        else:
            current_material *= 2
            current_magic_level *= 2
        current_sum = current_material + current_magic_level
    elif current_sum >= 500:
        current_material /= 2
        current_magic_level /= 2
        current_sum = current_material + current_magic_level

    if 100 <= current_sum < 500:
        if int(current_sum) in MAPPER["Gemstone"]:
            presents_dict["Gemstone"] += 1
        elif int(current_sum) in MAPPER["Porcelain Sculpture"]:
            presents_dict["Porcelain Sculpture"] += 1
        elif int(current_sum) in MAPPER["Gold"]:
            presents_dict["Gold"] += 1
        elif int(current_sum) in MAPPER["Diamond Jewellery"]:
            presents_dict["Diamond Jewellery"] += 1


if (presents_dict["Gemstone"] and presents_dict["Porcelain Sculpture"]) or \
        (presents_dict["Gold"] and presents_dict["Diamond Jewellery"]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(el) for el in magic_levels])}")

presents_dict = dict(sorted(presents_dict.items(), key=lambda x: x[0]))

for gift_type, quantity in presents_dict.items():
    if not presents_dict[gift_type] == 0:
        print(f"{gift_type}: {quantity}")
