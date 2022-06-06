divisor = int(input())
boundary = int(input())

number = ""

if boundary % divisor == 0:
    number = boundary
    print(number)
elif boundary % divisor != 0:
    while boundary % divisor != 0:
        boundary -= 1
    else:
        print(boundary)
