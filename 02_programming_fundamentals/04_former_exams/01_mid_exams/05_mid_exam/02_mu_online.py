def potion_command(f_dungeon_rooms, f_health):
    amount = int(f_dungeon_rooms[1])
    lack_of_health = 100 - f_health
    if amount > lack_of_health:
        f_health = 100
        print(f"You healed for {lack_of_health} hp.")
    else:
        f_health += amount
        print(f"You healed for {amount} hp.")
    print(f"Current health: {f_health} hp.")
    return f_health


def chest_command(f_dungeon_rooms, f_bitcoins):
    found_bitcoins = int(f_dungeon_rooms[1])
    f_bitcoins += found_bitcoins
    print(f"You found {found_bitcoins} bitcoins.")
    return f_bitcoins


def other_command(f_dungeon_rooms, f_health, dead_status):
    monster = f_dungeon_rooms[0]
    attack = int(f_dungeon_rooms[1])
    left_health = f_health - attack
    if left_health > 0:
        f_health = left_health
        print(f"You slayed {monster}.")
    else:
        dead_status = True
        f_health = 0
        print(f"You died! Killed by {monster}.")
    return f_health, dead_status


health = 100
bitcoin_amount = 0
dungeon_rooms = input().split("|")
is_dead = False

for room in range(len(dungeon_rooms)):
    current_room = dungeon_rooms[room].split()
    command = current_room[0]
    if command == "potion":
        health = potion_command(current_room, health)
    elif command == "chest":
        bitcoin_amount = chest_command(current_room, bitcoin_amount)
    else:
        health, is_dead = other_command(current_room, health, is_dead)
        if is_dead:
            print(f"Best room: {room + 1}")
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin_amount}")
    print(f"Health: {health}")
