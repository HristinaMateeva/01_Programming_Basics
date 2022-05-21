moves = int(input())

total_points = 0
num_0_to_9 = 0
num_10_to_19 = 0
num_20_to_29 = 0
num_30_to_39 = 0
num_40_to_50 = 0
invalid_numbers = 0

for num in range(1, moves + 1):
    current_moves = int(input())
    if 0 <= current_moves <= 9:
        num_0_to_9 += 1
        total_points = total_points + (current_moves * 0.20)
    elif 10 <= current_moves <= 19:
        num_10_to_19 += 1
        total_points = total_points + (current_moves * 0.30)
    elif 20 <= current_moves <= 29:
        num_20_to_29 += 1
        total_points = total_points + (current_moves * 0.40)
    elif 30 <= current_moves <= 39:
        num_30_to_39 += 1
        total_points += 50
    elif 40 <= current_moves <= 50:
        num_40_to_50 += 1
        total_points += 100
    else:
        invalid_numbers += 1
        total_points /= 2

total_nums = num_0_to_9 + num_10_to_19 + num_20_to_29 + num_30_to_39 + num_40_to_50 + invalid_numbers
percent_0_to_9 = num_0_to_9 / total_nums * 100
percent_10_to_19 = num_10_to_19 / total_nums * 100
percent_20_to_29 = num_20_to_29 / total_nums * 100
percent_30_to_39 = num_30_to_39 / total_nums * 100
percent_40_to_50 = num_40_to_50 / total_nums * 100
percent_invalid_numbers = invalid_numbers / total_nums * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid_numbers:.2f}%")
