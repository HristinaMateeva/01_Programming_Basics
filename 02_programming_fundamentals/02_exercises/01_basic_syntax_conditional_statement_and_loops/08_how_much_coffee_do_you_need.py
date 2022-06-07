command = input()

counter_coffee = 0
extra_sleep_needed = False

while not command == "END":
    if command.lower() == "coding":
        if command.islower():
            counter_coffee += 1
        elif command.isupper():
            counter_coffee += 2
    elif command.lower() == "dog" or command.lower() == "cat":
        if command.islower():
            counter_coffee += 1
        elif command.isupper():
            counter_coffee += 2
    elif command.lower() == "movie":
        if command.islower():
            counter_coffee += 1
        elif command.isupper():
            counter_coffee += 2

    if counter_coffee > 5:
        extra_sleep_needed = True
        break
    command = input()

if extra_sleep_needed:
    print("You need extra sleep")
else:
    print(counter_coffee)
