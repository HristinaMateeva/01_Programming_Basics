count_of_numbers = int(input())
sum_of_all_elements = 0
max_number = " "
for number in range(count_of_numbers):  #range(1, count_of_numbers + 1)
    current_number = int(input())
    if number == 0:
        max_number = current_number
    sum_of_all_elements += current_number
    if current_number > max_number:
        max_number = current_number
#max_number == sum_of_all_elements / 2 - ни дава число float
if max_number == sum_of_all_elements - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (sum_of_all_elements - max_number))
    print("No")
    print(f"Diff = {difference}")
