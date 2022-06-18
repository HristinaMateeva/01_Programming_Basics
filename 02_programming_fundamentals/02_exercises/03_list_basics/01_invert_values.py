single_string = input().split()

single_string_as_int = [int(el) for el in single_string]
result = []

for el in single_string_as_int:
    opposite_el = el * -1
    result.append(opposite_el)

print(result)
