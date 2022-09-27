def cast_shell_command(f_heroes_data, f_command):
    name = f_command[1]
    mana_points_needed = int(f_command[2])
    spell_name = f_command[3]
    if f_heroes_data[name]["MP"] >= mana_points_needed:
        f_heroes_data[name]["MP"] -= mana_points_needed
        print(f'{name} has successfully cast {spell_name} and now has {f_heroes_data[name]["MP"]} MP!')
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    return f_heroes_data


def take_damage_command(f_heroes_data, f_command):
    name = f_command[1]
    damage = int(f_command[2])
    attacker = f_command[3]
    if f_heroes_data[name]["HP"] > damage:
        f_heroes_data[name]["HP"] -= damage
        print(f'{name} was hit for {damage} HP by {attacker} and now has {f_heroes_data[name]["HP"]} HP left!')
    else:
        del f_heroes_data[name]
        print(f"{name} has been killed by {attacker}!")
    return f_heroes_data


def recharge_command(f_heroes_data, f_command):
    name = f_command[1]
    amount = int(f_command[2])
    if (f_heroes_data[name]["MP"] + amount) > 200:
        amount_recovered = 200 - f_heroes_data[name]["MP"]
        f_heroes_data[name]["MP"] = 200
    else:
        f_heroes_data[name]["MP"] += amount
        amount_recovered = amount
    print(f"{name} recharged for {amount_recovered} MP!")
    return f_heroes_data


def heal_command(f_heroes_data, f_command):
    name = f_command[1]
    amount = int(f_command[2])
    if (f_heroes_data[name]["HP"] + amount) > 100:
        amount_recovered = 100 - f_heroes_data[name]["HP"]
        f_heroes_data[name]["HP"] = 100
    else:
        f_heroes_data[name]["HP"] += amount
        amount_recovered = amount
    print(f"{name} healed for {amount_recovered} HP!")
    return f_heroes_data


num_heroes = int(input())

heroes_data = {}

for num in range(num_heroes):
    initial_command = input().split()
    hero_name = initial_command[0]
    hero_hit_points = int(initial_command[1])
    hero_mana_points = int(initial_command[2])
    heroes_data[hero_name] = {"HP": hero_hit_points, "MP": hero_mana_points}

command = input()

while not command == "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        heroes_data = cast_shell_command(heroes_data, command)
    elif command[0] == "TakeDamage":
        heroes_data = take_damage_command(heroes_data, command)
    elif command[0] == "Recharge":
        heroes_data = recharge_command(heroes_data, command)
    elif command[0] == "Heal":
        heroes_data = heal_command(heroes_data, command)
    command = input()

for hero, skills in heroes_data.items():
    print(f"{hero}")
    print(f'  HP: {heroes_data[hero]["HP"]}')
    print(f'  MP: {heroes_data[hero]["MP"]}')
