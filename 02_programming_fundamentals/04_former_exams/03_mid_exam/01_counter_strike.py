energy = int(input())
command = input()

is_game_lost = False
counter_won_games = 0

while not command == "End of battle":
    distance = int(command)
    if energy < distance:
        is_game_lost = True
        break
    energy -= distance
    counter_won_games += 1
    if counter_won_games % 3 == 0:
        energy += counter_won_games
    command = input()

if is_game_lost:
    print(f"Not enough energy! Game ends with {counter_won_games} won battles and {energy} energy")
else:
    print(f"Won battles: {counter_won_games}. Energy left: {energy}")
