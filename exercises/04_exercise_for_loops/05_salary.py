num_open_tabs = int(input())
salary_amount = int(input())
left_money = 0
for number in range(1, num_open_tabs + 1):
    tab = input()
    if tab == "Facebook":
        salary_amount -= 150
    elif tab == "Instagram":
        salary_amount -= 100
    elif tab == "Reddit":
        salary_amount -= 50
    if salary_amount == 0:
        break
if salary_amount <= 0:
    print(f"You have lost your salary.")
elif salary_amount > 0:
    print(f"{salary_amount:2d}")
