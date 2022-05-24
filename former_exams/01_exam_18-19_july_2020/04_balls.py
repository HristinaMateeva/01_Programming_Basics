import math

num_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colours_balls = 0

for num in range(1, num_balls + 1):
    ball = input()
    if ball == "red":
        total_points += 5
        red_balls += 1
    elif ball == "orange":
        total_points += 10
        orange_balls += 1
    elif ball == "yellow":
        total_points += 15
        yellow_balls += 1
    elif ball == "white":
        total_points += 20
        white_balls += 1
    elif ball == "black":
        total_points /= 2
        black_balls += 1
    else:
        other_colours_balls += 1
        continue

print(f"Total points: {math.floor(total_points)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_colours_balls}")
print(f"Divides from black balls: {black_balls}")
