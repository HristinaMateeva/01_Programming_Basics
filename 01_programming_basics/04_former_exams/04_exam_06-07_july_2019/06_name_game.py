command = input()

max_points = 0
winner_name = " "

while command != "Stop":
    player_name = command
    player_points = 0
    for letter in player_name:
        number = int(input())
        if number == ord(letter):
            player_points += 10
        else:
            player_points += 2
    if player_points >= max_points:
        max_points = player_points
        winner_name = player_name
    command = input()

print(f"The winner is {winner_name} with {max_points} points!")
