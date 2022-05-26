voucher_amount = int(input())
command = input()

counter_tickets = 0
sum_tickets = 0
counter_others = 0
sum_others = 0

while command != "End":
    name_purchase = command
    price_purchase = len(name_purchase)
    if price_purchase > 8:
        sum_tickets = ord(name_purchase[0]) + ord(name_purchase[1])
        voucher_amount -= sum_tickets
        if voucher_amount <= 0:
            break
        counter_tickets += 1
    elif price_purchase <= 8:
        sum_others = ord(name_purchase[0])
        voucher_amount -= sum_others
        if voucher_amount <= 0:
            break
        counter_others += 1

    command = input()

print(f"{counter_tickets}")
print(f"{counter_others}")

