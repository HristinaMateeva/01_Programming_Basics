line = input()

index = 0

while index < len(line) - 1:
    if line[index] == line[index + 1]:
        line = line.replace(line[index] + line[index + 1], line[index])
        index = 0
    else:
        index += 1

print(line)
