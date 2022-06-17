data = [1, 12.5, False, "Hello", 2]

list_only_integers = []

for el in data:
    if isinstance(el, int) and not isinstance(el, bool):
        list_only_integers.append(el)

print(list_only_integers)
