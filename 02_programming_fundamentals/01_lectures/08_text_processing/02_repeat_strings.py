sequence = input().split()

result = ""

for word in sequence:
    length = len(word)
    result += word * length

print(result)
