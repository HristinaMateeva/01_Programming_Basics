maiden_party_price = float(input())
num_love_letters = int(input())
num_roses = int(input())
num_key_chains = int(input())
num_cartoons = int(input())
num_lucky_surprises = int(input())

love_letters = 0.60
roses = 7.20
key_chain = 3.60
cartoons = 18.20
lucky_surprise = 22

num_total = num_love_letters + num_roses + num_key_chains + num_cartoons + num_lucky_surprises
total_sum = num_love_letters * love_letters + num_roses * roses + num_key_chains * key_chain + \
            num_cartoons * cartoons + num_lucky_surprises * lucky_surprise
if num_total >= 25:
    total_sum *= 0.65

total_sum *= 0.90
difference = abs(maiden_party_price - total_sum)

if total_sum >= maiden_party_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
