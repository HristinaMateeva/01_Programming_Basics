def validation_data(dragon_damage, dragon_health, dragon_armor):
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    return int(dragon_damage), int(dragon_health), int(dragon_armor)


num_dragons = int(input())
final_data = {}
average_results = {}

for num in range(num_dragons):
    command = input().split()
    dragon_type = command[0]
    dragon_name = command[1]
    damage = command[2]
    health = command[3]
    armor = command[4]
    damage, health, armor = validation_data(damage, health, armor)
    if dragon_type not in final_data:
        final_data[dragon_type] = {dragon_name: []}
    elif dragon_name not in final_data[dragon_type]:
        final_data[dragon_type][dragon_name] = []
    final_data[dragon_type][dragon_name] = [damage, health, armor]

for side, dragons in final_data.items():
    final_data[side] = dict(sorted(dragons.items(), key=lambda kvp: kvp[0]))
    side_sum_damage = 0
    side_sum_health = 0
    side_sum_armor = 0
    for dragon, skills in dragons.items():
        side_sum_damage += skills[0]
        side_sum_health += skills[1]
        side_sum_armor += skills[2]
    average_damage = side_sum_damage / len(dragons)
    average_health = side_sum_health / len(dragons)
    average_armor = side_sum_armor / len(dragons)
    average_results[side] = [average_damage, average_health, average_armor]

for type_side, av_result in average_results.items():
    print(f"{type_side}::({av_result[0]:.2f}/{av_result[1]:.2f}/{av_result[2]:.2f})")
    for dragon_side, dragon_ids in final_data.items():
        if type_side == dragon_side:
            for dragon_id, all_skills in dragon_ids.items():
                print(f"-{dragon_id} -> damage: {all_skills[0]}, health: {all_skills[1]}, armor: {all_skills[2]}")
