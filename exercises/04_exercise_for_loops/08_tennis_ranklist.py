import math
num_tournaments = int(input())
initial_points = int(input())
total_points = initial_points
won_tournaments = 0
for tournaments in range (1, num_tournaments + 1):
    position = input()
    if position == "W":
        total_points += 2000
        won_tournaments += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":
        total_points += 720
average_points = (total_points - initial_points) / num_tournaments
percent_won_tournaments = won_tournaments / num_tournaments * 100
print(f"Final points: {math.floor(total_points)}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_won_tournaments:.2f}%")
