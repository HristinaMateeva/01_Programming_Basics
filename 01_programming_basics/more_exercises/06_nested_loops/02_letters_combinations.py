first_letter = input()
second_letter = input()
third_letter = input()  

exclusion = False
counter = 0
result = " "

for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if i == ord(third_letter) or j == ord(third_letter) or k == ord(third_letter):
                exclusion = True
                continue
            counter += 1
            result += ('' + chr(i) + chr(j) + chr(k) + ' ')

print(f"{result}{counter}")
