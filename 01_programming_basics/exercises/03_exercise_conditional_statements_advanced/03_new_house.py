type_of_flower = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if type_of_flower == "Roses":
    price = number_of_flowers * 5
elif type_of_flower == "Dahlias":
    price = number_of_flowers * 3.80
elif type_of_flower == "Tulips":
    price = number_of_flowers * 2.80
elif type_of_flower == "Narcissus":
    price = number_of_flowers * 3
elif type_of_flower == "Gladiolus":
    price = number_of_flowers * 2.50
if type_of_flower == "Roses" and number_of_flowers > 80:
    price *= 0.90
elif type_of_flower == "Dahlias" and number_of_flowers > 90:
    price *= 0.85
elif type_of_flower == "Tulips" and number_of_flowers > 80:
    price *= 0.85
elif type_of_flower == "Narcissus" and number_of_flowers < 120:
    price *= 1.15
elif type_of_flower == "Gladiolus" and number_of_flowers < 80:
    price *= 1.20
difference = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
