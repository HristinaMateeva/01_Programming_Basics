budget = int(input())
command = input()

while not command == "End":
    price = int(command)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break

    command = input()

else:
    print("You bought everything needed.")
