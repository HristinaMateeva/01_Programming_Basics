text = input()

encrypted_version = ""

for el in text:
    changed_char = chr(ord(el) + 3)
    encrypted_version += changed_char

print(encrypted_version)
