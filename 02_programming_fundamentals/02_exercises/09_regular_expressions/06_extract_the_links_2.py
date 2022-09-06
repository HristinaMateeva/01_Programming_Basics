import re

data = input()
# pattern = r"(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))" - the zero test 2 is incorrect
pattern = r"(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"

while data:
    for el in re.finditer(pattern, data):
        print(el.group())
    data = input()
