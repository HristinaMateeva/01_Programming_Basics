initial_message = input()

emoticon = ""

for index in range(len(initial_message)):
    if initial_message[index] == ":":
        emoticon = ":" + initial_message[index + 1]
        print(emoticon)
