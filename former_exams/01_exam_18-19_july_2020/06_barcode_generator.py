range_beginning = int(input())
range_end = int(input())

range_one = str(range_beginning)
range_two = str(range_end)

for i in range(range_beginning, range_end + 1):
    number_as_string = str(i)
    counter = 0
    for index, digit in enumerate(number_as_string):
        if int(digit) % 2 == 0:
            break
        elif int(range_one[index]) <= int(digit) <= int(range_two[index]):
            counter += 1
    if counter == 4:
        print(i, end= " ")
