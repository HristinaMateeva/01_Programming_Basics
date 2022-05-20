season = input()
type_group = input()
num_students = int(input())
num_nights = int(input())

sport = " "
price_per_student = 0
total_price = 0

if season == "Winter":
    if type_group == "girls":
        sport = "Gymnastics"
        price_per_student = num_nights * 9.60
    elif type_group == "boys":
        sport = "Judo"
        price_per_student = num_nights * 9.60
    elif type_group == "mixed":
        sport = "Ski"
        price_per_student = num_nights * 10
elif season == "Spring":
    if type_group == "girls":
        sport = "Athletics"
        price_per_student = num_nights * 7.20
    elif type_group == "boys":
        sport = "Tennis"
        price_per_student = num_nights * 7.20
    elif type_group == "mixed":
        sport = "Cycling"
        price_per_student = num_nights * 9.50
elif season == "Summer":
    if type_group == "girls":
        sport = "Volleyball"
        price_per_student = num_nights * 15
    elif type_group == "boys":
        sport = "Football"
        price_per_student = num_nights * 15
    elif type_group == "mixed":
        sport = "Swimming"
        price_per_student = num_nights * 20

total_price = num_students * price_per_student

if num_students >= 50:
    total_price *= 0.5
elif num_students >= 20 and num_students < 50:
    total_price *= 0.85
elif num_students >= 10 and num_students < 20:
    total_price *= 0.95
print(f"{sport} {total_price:.2f} lv.")
