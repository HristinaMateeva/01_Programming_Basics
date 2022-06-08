n = int(input())

number_is_even = True

for i in range(n):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        number_is_even = False
        break

if number_is_even:
    print("All numbers are even.")
