line = input().split(">")
explode = 0
after_explode = []

for element in line:
    if element[0].isdigit():
        explode += int(element[0])
        if len(element) <= explode:
            explode -= len(element)
            element = ">"
        else:
            element = ">" + "".join(list(element[explode::]))
            explode = 0
    after_explode.append(element)
print("".join(after_explode))
