text = input()

reversed_text = ""

while not text == "end":
    reversed_text = text[::-1]
    print(f"{text} = {reversed_text}")
    text = input()
