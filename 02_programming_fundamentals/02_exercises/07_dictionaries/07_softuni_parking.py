num_commands = int(input())

registered_cars = {}

for num in range(num_commands):
    command = input().split()
    if "register" in command:
        username = command[1]
        plate_number = command[2]
        if username in registered_cars:
            print(f"ERROR: already registered with plate number {registered_cars[username]}")
        else:
            registered_cars[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif "unregister" in command:
        username = command[1]
        if username not in registered_cars:
            print(f"ERROR: user {username} not found")
        else:
            del registered_cars[username]
            print(f"{username} unregistered successfully")

for user, reg_plate in registered_cars.items():
    print(f"{user} => {reg_plate}")
