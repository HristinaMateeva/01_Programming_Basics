import re

data = input()
pattern = r"\d+"
current_list = []
current_string = ""

while data:
    current_list.append(data)
    current_string = ' '.join(current_list)

    data = input()

result = re.findall(pattern, current_string)
print(' '.join(result))
