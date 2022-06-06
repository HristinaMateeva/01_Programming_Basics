num_messages = int(input())

for num in range(num_messages):
    message_code = int(input())

    if message_code == 88:
        print("Hello")
    elif message_code == 86:
        print("How are you?")
    elif message_code < 88:
        print("GREAT!")
    elif message_code > 88:
        print("Bye.")
