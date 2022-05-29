annual_tax = int(input())
sneakers_price = annual_tax - (annual_tax * 0.4)    #annual_tax * 0.60
outfit_price = sneakers_price - (sneakers_price * 0.2)   #sneakers_price * 0.80
ball_price = outfit_price / 4   #*1 / 4
accessories_price = ball_price / 5  # * 1 / 5
equipment_price = sneakers_price + outfit_price + ball_price + accessories_price
needed_sum = annual_tax + equipment_price
print(needed_sum)
