enrolled_heroes = input()
heroes = {}

while enrolled_heroes != "End":
    split_command = enrolled_heroes.split(" ")
    if split_command[0] == "Enroll":
        hero_name = split_command[1]
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif split_command[0] == "Learn":
        hero_name = split_command[1]
        spell_name = split_command[2]
        if hero_name in heroes:
            if spell_name not in heroes[hero_name]:
                heroes[hero_name] += [spell_name]
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

        # if hero_name not in heroes:
        #     print(f"{hero_name} doesn't exist.")
        # if spell_name in heroes[hero_name]:
        #     print(f"{hero_name} has already learnt {spell_name}.")
        # else:
        #     heroes[hero_name] = [spell_name]

    elif split_command[0] == "Unlearn":
        hero_name = split_command[1]
        spell_name = split_command[2]
        if hero_name in heroes:
            if spell_name in heroes[hero_name]:              #Change
                heroes[hero_name].remove(spell_name)         #Change
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")

    enrolled_heroes = input()

print(f"Heroes:")
for hero, spell in heroes.items():
    spells = "".join(spell)
    print(f"== {hero}: {spells}")
