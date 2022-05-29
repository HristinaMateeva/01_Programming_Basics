heritage_money = float(input())
year_in_the_past = int(input())
left_money = heritage_money
spent_money = 0
age = 17

for num in range(1800, year_in_the_past + 1):
    if num % 2 == 0:
        age += 1
        spent_money = 12000
        left_money -= spent_money
    elif num % 2 == 1:
        age += 1
        spent_money = 12000 + (age * 50)
        left_money -= spent_money

if left_money >= 0:
    print(f"Yes! He will live a carefree life and will have {abs(left_money):.2f} dollars left.")
elif left_money < 0:
    print(f"He will need {abs(left_money):.2f} dollars to survive.")
