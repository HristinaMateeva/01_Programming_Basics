command = input()

toy_price = 5
sweaters_price = 15
counter_kids = 0
counter_adults = 0
total_price_kids = 0
total_price_adults = 0

while command != "Christmas":
    command = int(command)
    if command <= 16:
        counter_kids += 1
        total_price_kids += toy_price
    elif command > 16:
        counter_adults += 1
        total_price_adults += sweaters_price

    command = input()

print(f"Number of adults: {counter_adults}")
print(f"Number of kids: {counter_kids}")
print(f"Money for toys: {total_price_kids}")
print(f"Money for sweaters: {total_price_adults}")
