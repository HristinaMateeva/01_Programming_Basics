import re

valid_urls = []
pattern = r"((w{3})\.([A-Za-z0-9]+)(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"

sentence = input()

while sentence:
    matches = re.finditer(pattern, sentence)
    sentence = input()
    for match in matches:
        valid_urls.append(match.group(1))

for valid_url in valid_urls:
    print(valid_url)
