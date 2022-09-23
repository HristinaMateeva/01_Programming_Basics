days_of_adventure = int(input())
num_of_players = int(input())
group_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())

no_more_energy = False
total_water_per_day = water_per_person * num_of_players * days_of_adventure
total_food_per_day = food_per_person * num_of_players * days_of_adventure
for day in range(1, days_of_adventure + 1):
    energy_loss_per_day = float(input())
    group_energy -= energy_loss_per_day
    if group_energy <= 0:
        no_more_energy = True
        break
    if day % 2 == 0:
        group_energy += (group_energy * 0.05)
        total_water_per_day -= total_water_per_day * 0.3
    if day % 3 == 0:
        total_food_per_day -= (total_food_per_day / num_of_players)
        group_energy += (group_energy * 0.10)

if no_more_energy:
    print(f"You will run out of energy. You will be left with {total_food_per_day:.2f} food and {total_water_per_day:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
