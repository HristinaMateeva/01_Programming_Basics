command = input()

contacts_list = {}

while not command.isdigit():
    contact_name, phone_number = command.split("-")
    contacts_list[contact_name] = phone_number

    command = input()

for num in range(1, int(command) + 1):
    name = input()
    if name in contacts_list:
        print(f"{name} -> {contacts_list.get(name)}")
    else:
        print(f"Contact {name} does not exist.")
