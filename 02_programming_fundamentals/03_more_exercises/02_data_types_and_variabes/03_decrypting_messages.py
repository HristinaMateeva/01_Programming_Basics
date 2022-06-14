key_integer = int(input())
num_lines = int(input())

result = ""

for num in range(num_lines):
    letter = input()
    decrypted_letter = chr(ord(letter) + key_integer)
    print(f"{decrypted_letter}", end="")
