number_sold_games = int(input())

counter_hearthstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_others = 0

for num in range(1, number_sold_games + 1):
    game_name = input()
    if game_name == "Hearthstone":
        counter_hearthstone += 1
    elif game_name == "Fornite":
        counter_fornite += 1
    elif game_name == "Overwatch":
        counter_overwatch += 1
    else:
        counter_others += 1

percent_hearthstone = counter_hearthstone / number_sold_games * 100
percent_fornite = counter_fornite / number_sold_games * 100
percent_overwatch = counter_overwatch / number_sold_games * 100
percent_others = counter_others / number_sold_games * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
