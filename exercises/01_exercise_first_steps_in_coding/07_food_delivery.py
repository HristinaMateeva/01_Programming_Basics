chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price_of_chicken_menu = 10.35
price_of_fish_menu = 12.40
price_of_vegetarian_menu = 8.15
sum_without_discount = chicken_menu * price_of_chicken_menu + \
                       fish_menu * price_of_fish_menu + \
                       vegetarian_menu * price_of_vegetarian_menu
price_of_dessert = sum_without_discount * 0.20
delivery_fee = 2.50
sum_total = sum_without_discount + price_of_dessert + delivery_fee
print(sum_total)
