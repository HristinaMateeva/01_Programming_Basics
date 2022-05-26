total_months = int(input())

bill_electricity = 0
total_bill_electricity = 0
bill_water = 0
bill_internet = 0
other_bills = 0
total_bills = 0

for month in range (1, total_months + 1):
    bill_electricity = float(input())
    total_bill_electricity += bill_electricity
    bill_water += 20
    bill_internet += 15
    other_bills += (bill_electricity + 20 + 15) * 1.20

average = (total_bill_electricity + bill_water + bill_internet + other_bills) / total_months
print(f"Electricity: {total_bill_electricity:.2f} lv")
print(f"Water: {bill_water:.2f} lv")
print(f"Internet: {bill_internet:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")
