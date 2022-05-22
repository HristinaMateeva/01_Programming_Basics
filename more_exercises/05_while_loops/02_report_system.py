needed_sum_charity = int(input())
price_product = input()

counter = 0
counter_cash = 0
counter_credit_card = 0
cash_payments = 0
credit_card_payments = 0
total_sum = 0
is_charity_ended = False
average_cash = 0
average_credit_card = 0

while price_product != "End":
    price = int(price_product)
    counter += 1
    if counter % 2 == 1:  # Type of payment: Cash
        if price > 100:
            print("Error in transaction!")
        else:
            cash_payments += price
            counter_cash += 1
            print("Product sold!")
            total_sum += price
            average_cash = cash_payments / counter_cash
    elif counter % 2 == 0:  # Type of payment: Credit card 
        if price < 10:
            print("Error in transaction!")
        else:
            credit_card_payments += price
            counter_credit_card += 1
            print("Product sold!")
            total_sum += price
            average_credit_card = credit_card_payments / counter_credit_card
    if total_sum >= needed_sum_charity:
        is_charity_ended = True
        break
    price_product = input()

if is_charity_ended:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_credit_card:.2f}")
else:
    print("Failed to collect required money for charity.")
