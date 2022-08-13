message = input()

result = ""

for el in message:
    result += chr(ord(el) + 3)

print(result)
