text = input()

while ":" in text:
    index = text.find(":")
    print(text[index:index + 2])
    text = text.replace(":", "", 1)
