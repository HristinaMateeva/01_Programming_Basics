command = input()

dwarf_data = {}
result_data = {}

while not command == "Once upon a time":
    name, hat_colour, physics = command.split(" <:> ")
    physics = int(physics)
    if hat_colour not in dwarf_data:
        dwarf_data[hat_colour] = {name: physics}
    elif name not in dwarf_data[hat_colour] or dwarf_data[hat_colour][name] < physics:
        dwarf_data[hat_colour][name] = physics
    command = input()

for colour, names in dwarf_data.items():
    for name_id, physics_id in names.items():
        if physics_id not in result_data:
            result_data[physics_id] = {colour: []}
        elif colour not in result_data[physics_id]:
            result_data[physics_id][colour] = []
        result_data[physics_id][colour].append(name_id)

result_data = dict(sorted(result_data.items(), key=lambda kvp: -kvp[0]))
for key, values in result_data.items():
    result_data[key] = dict(sorted(values.items(), key=lambda kvp: -len(kvp[1])))

for physic, colours_id in result_data.items():
    for colour_id, name_id in colours_id.items():
        for dwarf_name in name_id:
            print(f"({colour_id}) {dwarf_name} <-> {physic}")

# 90% in Judge
