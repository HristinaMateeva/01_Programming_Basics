word = input()

result = ""

while not word == "End":
    for index in word:
        if word == "SoftUni":
            break
        else:
            result += index * 2
    if result:
        print(result)

    result = ""
    word = input()
