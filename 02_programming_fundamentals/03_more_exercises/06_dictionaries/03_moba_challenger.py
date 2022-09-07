command = input()

season_data = {}
max_points_per_user = {}
# is_won = False

while not command == "Season end":
    is_won = False
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in season_data:
            season_data[player] = {position: skill}
        elif position not in season_data[player] or season_data[player][position] < skill:
            season_data[player][position] = skill
    else:
        player_1, player_2 = command.split(" vs ")
        if player_1 in season_data and player_2 in season_data:
            for player_one, position_1 in season_data.items():
                for player_two, position_2 in season_data.items():
                    if player_1 == player_one and player_2 == player_two:
                        for position_one, skill_one in position_1.items():
                            for position_two, skill_two in position_2.items():
                                if position_one == position_two and skill_one > skill_two:
                                    is_won = True
                                    del season_data[player_two]
                                    break
                                elif position_one == position_two and skill_one < skill_two:
                                    is_won = True
                                    del season_data[player_one]
                                    break
                            if is_won:
                                break
                    if is_won:
                        break
                if is_won:
                    break
    command = input()

for user, data_per_user in season_data.items():
    season_data[user] = dict(sorted(data_per_user.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for data, points in data_per_user.items():
        if user not in max_points_per_user:
            max_points_per_user[user] = points
        else:
            max_points_per_user[user] += points

max_points_per_user = dict(sorted(max_points_per_user.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for username, max_points in max_points_per_user.items():
    print(f"{username}: {max_points} skill")
    for user_id, positions in season_data.items():
        if username == user_id:
            for pos, results in positions.items():
                print(f"- {pos} <::> {results}")
