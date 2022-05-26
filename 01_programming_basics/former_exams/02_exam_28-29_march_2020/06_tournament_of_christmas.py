number_days = int(input())

raised_money_per_day = 0
total_raised_money = 0
counter_total_wins = 0
counter_total_lost = 0
# is_tournament_continue = True

for days in range(1, number_days + 1):
    command = input()
    raised_money_per_day = 0
    counter_won_games_per_day = 0
    counter_lost_games_per_day = 0
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            raised_money_per_day += 20
            counter_won_games_per_day += 1
            counter_total_wins += counter_won_games_per_day
        elif result == "lose":
            counter_lost_games_per_day += 1
            counter_total_lost += counter_lost_games_per_day

        command = input()
    if counter_won_games_per_day > counter_lost_games_per_day:
        raised_money_per_day *= 1.10
    total_raised_money += raised_money_per_day
if counter_total_wins > counter_total_lost:
    total_raised_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_raised_money:.2f}")
