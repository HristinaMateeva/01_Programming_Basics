from simple_operations.helper import operation_mapper

data = input().split()

a = float(data[0])
sign = data[1]
b = float(data[2])

try:
    print(operation_mapper[sign](a,b))
except ZeroDivisionError:
    print("Invalid number b. Should not be 0 if divide")
