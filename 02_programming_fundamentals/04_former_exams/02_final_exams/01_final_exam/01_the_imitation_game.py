encrypted_message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    if command[0] == "Move":
        num_letters = int(command[1])
        left_side = encrypted_message[:num_letters]
        right_side = encrypted_message[num_letters:]
        encrypted_message = right_side + left_side
    elif command[0] == "Insert":
        insert_index = int(command[1])
        insert_value = command[2]
        left_side = encrypted_message[:insert_index]
        right_side = encrypted_message[insert_index:]
        encrypted_message = left_side + insert_value + right_side
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")
