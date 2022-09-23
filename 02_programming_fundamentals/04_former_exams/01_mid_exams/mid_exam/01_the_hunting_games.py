adventure_days = int(input())
number_players = int(input())
energy_of_the_group = float(input())
water_per_person_per_day = float(input())
food_per_person_per_days = float(input())

total_water = water_per_person_per_day * number_players * adventure_days
total_food = food_per_person_per_days * number_players * adventure_days

left_energy = True

for day in range(1, adventure_days + 1):
    chop_wood_energy_loss = float(input())
    energy_of_the_group -= chop_wood_energy_loss
    if energy_of_the_group <= 0:
        left_energy = False
        break
    if day % 2 == 0:
        energy_of_the_group *= 1.05
        total_water *= 0.70
    if day % 3 == 0:
        energy_of_the_group *= 1.10
        total_food -= (total_food / number_players)

if not left_energy:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy_of_the_group:.2f} energy!")
