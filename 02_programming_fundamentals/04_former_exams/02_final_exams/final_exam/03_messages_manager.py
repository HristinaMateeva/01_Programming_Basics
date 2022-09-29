def add_command(f_messages_data, f_command):
    username = f_command[1]
    sent = int(f_command[2])
    received = int(f_command[3])
    if username not in f_messages_data:
        f_messages_data[username] = {'sent': sent, 'received': received}
    return f_messages_data


def message_command(f_messages_data, f_command, f_capacity):
    sender = f_command[1]
    receiver = f_command[2]
    if sender in f_messages_data and receiver in f_messages_data:
        f_messages_data[sender]['sent'] += 1
        f_messages_data[receiver]['received'] += 1
        if f_messages_data[sender]['sent'] + f_messages_data[sender]['received'] >= f_capacity:
            del f_messages_data[sender]
            print(f"{sender} reached the capacity!")
        if f_messages_data[receiver]['sent'] + f_messages_data[receiver]['received'] >= f_capacity:
            del f_messages_data[receiver]
            print(f"{receiver} reached the capacity!")
    return f_messages_data


def empty_command(f_messages_data, f_command):
    data_for_delete = f_command[1]
    if data_for_delete == "All":
        f_messages_data = {}
    elif data_for_delete in f_messages_data:
        del f_messages_data[data_for_delete]
    return f_messages_data


messages_capacity = int(input())
command = input()

messages_data = {}

while not command == "Statistics":
    command = command.split("=")
    if command[0] == "Add":
        messages_data = add_command(messages_data, command)
    elif command[0] == "Message":
        messages_data = message_command(messages_data, command, messages_capacity)
    elif command[0] == "Empty":
        messages_data = empty_command(messages_data, command)
    command = input()

print(f"Users count: {len(messages_data)}")
if messages_data:
    for user, data in messages_data.items():
        sum_messages = messages_data[user]['sent'] + messages_data[user]['received']
        print(f"{user} - {sum_messages}")
