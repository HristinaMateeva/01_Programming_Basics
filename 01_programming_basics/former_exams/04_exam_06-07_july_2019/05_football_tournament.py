football_team_name = input()
number_played_games = int(input())

is_played = True
counter_w = 0
counter_d = 0
counter_l = 0
counter_total = 0
bonus_points = 0
percent_win_rate = 0

if number_played_games == 0:
    is_played = False

for games in range(1, number_played_games + 1):
    match_result = input()
    if match_result == "W":
        counter_w += 1
        counter_total += 1
        bonus_points += 3
    elif match_result == "D":
        counter_d += 1
        counter_total += 1
        bonus_points += 1
    elif match_result == "L":
        counter_l += 1
        counter_total += 1
    percent_win_rate = counter_w / counter_total * 100

if not is_played:
    print(f"{football_team_name} hasn't played any games during this season.")
else:
    print(f"{football_team_name} has won {bonus_points} points during this season.")
    print("Total stats:")
    print(f"## W: {counter_w}")
    print(f"## D: {counter_d}")
    print(f"## L: {counter_l}")
    print(f"Win rate: {percent_win_rate:.2f}%")
