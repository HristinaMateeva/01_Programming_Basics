sent_off_players = input().split()

team_a = list(range(1, 12))
team_b = list(range(1, 12))

terminated = False

for card in sent_off_players:
    team, num_player = card.split("-")
    num_player = int(num_player)

    if team == "A" and num_player in team_a:
        team_a.remove(num_player)
    elif team == "B" and num_player in team_b:
        team_b.remove(num_player)
    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if terminated:
    print("Game was terminated")
