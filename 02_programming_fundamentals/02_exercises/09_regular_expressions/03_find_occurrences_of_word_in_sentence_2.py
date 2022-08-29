import re

data = input().lower()
searched_word = input().lower()

pattern = fr"\b{searched_word}\b"

result = len(re.findall(pattern, data))
print(result)
