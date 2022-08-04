legendary_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

while True:
    materials = input().split()
    is_found = False
    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        material = materials[index + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity
        for key, value in key_materials.items():
            if value >= 250:
                print(f"{legendary_materials[key]} obtained!")
                key_materials[key] -= 250
                is_found = True
                break
        if is_found:
            break
    if is_found:
        break

for key_1, value_1 in key_materials.items():
    print(f"{key_1}: {value_1}")
for key_2, value_2 in junk_materials.items():
    print(f"{key_2}: {value_2}")
