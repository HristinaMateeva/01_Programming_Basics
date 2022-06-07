quantity = int(input())
days = int(input())

ornament_set_price = 0
tree_skirt_price = 0
tree_garlands_price = 0
tree_lights_price = 0
christmas_spirit = 0
counter = 0

while counter < days:
    counter += 1
    if counter % 11 == 0:
        quantity += 2
    if counter % 2 == 0:
        ornament_set_price += 2 * quantity
        christmas_spirit += 5
    if counter % 3 == 0:
        tree_skirt_price += 5 * quantity
        tree_garlands_price += 3 * quantity
        christmas_spirit += 13
    if counter % 5 == 0:
        tree_lights_price += 15 * quantity
        christmas_spirit += 17
        if counter % 3 == 0:
            christmas_spirit += 30
    if counter % 10 == 0:
        christmas_spirit -= 20
        tree_skirt_price += 5
        tree_garlands_price += 3
        tree_lights_price += 15
        if counter == days:
            christmas_spirit -= 30

total_price = ornament_set_price + tree_garlands_price + tree_skirt_price + tree_lights_price
print(f'Total cost: {total_price}')
print(f'Total spirit: {christmas_spirit}')
