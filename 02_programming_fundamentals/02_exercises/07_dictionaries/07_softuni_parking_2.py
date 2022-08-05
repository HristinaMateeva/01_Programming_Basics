number = int(input())

registered_users = {}

for num in range(1, number + 1):
    command = input()
    if command.startswith("register"):
        registered, username, license_plate_num = command.split()
        if username in registered_users:
            print(f"ERROR: already registered with plate number {registered_users.get(username)}")
        else:
            registered_users[username] = license_plate_num
            print(f"{username} registered {license_plate_num} successfully")

    elif command.startswith("unregister"):
        unregistered, username = command.split()
        if not username in registered_users:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_users.pop(username)

for user, license_plate in registered_users.items():
    print(f"{user} => {license_plate}")
