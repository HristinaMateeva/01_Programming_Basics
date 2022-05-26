movie_name = input()
type_hall = input()
number_purchased_tickets = int(input())

total_price = 0
if movie_name == "A Star Is Born":
    if type_hall == "normal":
        total_price = number_purchased_tickets * 7.50
    elif type_hall == "luxury":
        total_price = number_purchased_tickets * 10.50
    elif type_hall == "ultra luxury":
        total_price = number_purchased_tickets * 13.50
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        total_price = number_purchased_tickets * 7.35
    elif type_hall == "luxury":
        total_price = number_purchased_tickets * 9.45
    elif type_hall == "ultra luxury":
        total_price = number_purchased_tickets * 12.75
elif movie_name == "Green Book":
    if type_hall == "normal":
        total_price = number_purchased_tickets * 8.15
    elif type_hall == "luxury":
        total_price = number_purchased_tickets * 10.25
    elif type_hall == "ultra luxury":
        total_price = number_purchased_tickets * 13.25
elif movie_name == "The Favourite":
    if type_hall == "normal":
        total_price = number_purchased_tickets * 8.75
    elif type_hall == "luxury":
        total_price = number_purchased_tickets * 11.55
    elif type_hall == "ultra luxury":
        total_price = number_purchased_tickets * 13.95

print(f"{movie_name} -> {total_price:.2f} lv.")
