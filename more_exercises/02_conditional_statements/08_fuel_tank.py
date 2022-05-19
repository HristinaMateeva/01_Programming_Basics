type_fuel = input()
liters_fuel = float(input())

if type_fuel == "Diesel":
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
elif type_fuel == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
elif type_fuel == "Gas":
    if liters_fuel >= 25:
        print(f"You have enough {type_fuel.lower()}.")
    elif liters_fuel < 25:
        print(f"Fill your tank with {type_fuel.lower()}!")
else:
    print(f"Invalid fuel!")
