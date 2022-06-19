list_of_strings = input().split()
n = int(input())

list_of_int = []
new_list = []

for element in list_of_strings:
    number = int(element)
    list_of_int.append(number)

list_of_int.sort()
list_of_int.reverse()

for index in range(n):
    list_of_int.pop()

for el in list_of_strings:
    if int(el) in list_of_int:
        new_list.append(el)

new_list = list(map(str, new_list))
print(", ".join(new_list))
