import re

pattern = r"^(\$|%)(?P<tag>[A-Z][a-z]{2,})\1:\s(?P<number>(\[[0-9]+\]\|){3})$"

number = int(input())

for num in range(number):
    valid_numbers = []
    nums = ""
    decrypted_message = ""
    message = input()
    matches = re.finditer(pattern, message)
    valid_match = re.findall(pattern, message)
    if valid_match:
        for match in matches:
            valid_dict = match.groupdict()
            nums = valid_dict['number']
            nums = nums.replace("[", "")
            nums = nums.replace("]", "")
            nums = nums.split("|")
            nums = [int(el) for el in nums[:3]]
            for element in nums:
                decrypted_message += chr(element)
            print(f"{valid_dict['tag']}: {decrypted_message}")
    else:
        print("Valid message not found!")
