num_bottles = int(input())
command = input()

num_plates = 0
num_pots = 0
counter = 0
total_ml_detergent = num_bottles * 750
needed_detergent = 0
is_finished_detergent = False

while command != "End":
    current_num_vessels = int(command)
    counter += 1
    if counter % 3 == 0:
        num_pots += current_num_vessels
        needed_detergent += current_num_vessels * 15
    else:
        num_plates += current_num_vessels
        needed_detergent += current_num_vessels * 5
    if needed_detergent > total_ml_detergent:
        is_finished_detergent = True
        break
    command = input()

difference = abs(needed_detergent - total_ml_detergent)

if is_finished_detergent:
    print(f"Not enough detergent, {difference} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{num_plates} dishes and {num_pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
