def odd_and_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for digit in num:
        if int(digit) % 2 == 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(odd_and_even_sum(number))
