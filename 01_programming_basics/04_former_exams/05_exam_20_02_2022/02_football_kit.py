t_shirt_price = float(input())
target_price = float(input())

shorts = t_shirt_price * 0.75
socks = shorts * 0.20
shoes = (t_shirt_price + shorts) * 2
total_sum = t_shirt_price + shorts + socks + shoes
discount_price = total_sum * 0.85

difference = abs(discount_price - target_price)

if discount_price >= target_price:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {discount_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
