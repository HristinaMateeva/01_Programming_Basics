destination = input()

while destination != "End":
    price_trip = float(input())

    sum_current_destination = 0 # sum се слага тук, а не отвън, защото сумата е за текущата дестинация
    while sum_current_destination < price_trip:
        saved_money = float(input())
        sum_current_destination += saved_money

    print(f"Going to {destination}!")

    destination = input()
