word = input()

result = ""

for i in range(len(word) - 1, -1, -1):
    result += word[i]

print(result)

#named argument: end=, start=, end=, step=