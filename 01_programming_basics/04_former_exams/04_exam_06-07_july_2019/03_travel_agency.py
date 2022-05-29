town_name = input()
type_package = input()
vip_discount = input()
number_days = int(input())

price_per_day = 0
total_price = 0
is_days_positive_number = True
is_town_valid = True
is_type_package_valid = True

if town_name == "Bansko" or town_name == "Borovets":
    if type_package == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.90
    elif type_package == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day *= 0.95
    else:
        is_type_package_valid = False
elif town_name == "Varna" or town_name == "Burgas":
    if type_package == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day *= 0.88
    elif type_package == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.93
    else:
        is_type_package_valid = False
else:
    is_town_valid = False

if number_days <= 0:
    is_days_positive_number = False
    print("Days must be positive number!")
elif number_days > 7 and is_town_valid and is_type_package_valid:
    total_price = price_per_day * (number_days - 1)
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif number_days <= 7 and is_town_valid and is_type_package_valid:
    total_price = price_per_day * number_days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
elif not is_town_valid:
    print("Invalid input!")
elif not is_type_package_valid:
    print("Invalid input!")
