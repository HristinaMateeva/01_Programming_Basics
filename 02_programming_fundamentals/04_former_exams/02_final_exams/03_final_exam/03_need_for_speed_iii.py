def drive_command(f_car_data, f_command):
    car = f_command[1]
    distance = int(f_command[2])
    fuel = int(f_command[3])
    if f_car_data[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        f_car_data[car]["mileage"] += distance
        f_car_data[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if f_car_data[car]["mileage"] >= 100000:
            del f_car_data[car]
            print(f"Time to sell the {car}!")
    return f_car_data


def refuel_command(f_car_data, f_command):
    car = f_command[1]
    fuel_to_refill = int(f_command[2])
    if (f_car_data[car]["fuel"] + fuel_to_refill) > max_reservoir_capacity:
        refilled_fuel = max_reservoir_capacity - f_car_data[car]["fuel"]
    else:
        refilled_fuel = fuel_to_refill
    f_car_data[car]["fuel"] += refilled_fuel
    print(f"{car} refueled with {refilled_fuel} liters")
    return f_car_data


def revert_command(f_car_data, f_command):
    car = f_command[1]
    kilometers = int(f_command[2])
    f_car_data[car]["mileage"] -= kilometers
    if f_car_data[car]["mileage"] < 10000:
        f_car_data[car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return f_car_data


number_of_cars = int(input())

car_data = {}
max_reservoir_capacity = 75

for num in range(number_of_cars):
    car_info = input().split("|")
    car_model = car_info[0]
    mileage = int(car_info[1])
    available_fuel = int(car_info[2])
    car_data[car_model] = {"mileage": mileage, "fuel": available_fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car_data = drive_command(car_data, command)
    elif command[0] == "Refuel":
        car_data = refuel_command(car_data, command)
    elif command[0] == "Revert":
        car_data = revert_command(car_data, command)
    command = input()

for model, data in car_data.items():
    print(f"{model} -> Mileage: {car_data[model]['mileage']} kms, Fuel in the tank: {car_data[model]['fuel']} lt.")
