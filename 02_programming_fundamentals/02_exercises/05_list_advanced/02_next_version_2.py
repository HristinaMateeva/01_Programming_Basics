current_version = input().split(".")

version_as_integers = [int(el) for el in current_version]

if not version_as_integers[2] == 9:
    version_as_integers[2] += 1
elif version_as_integers[2] == 9 and not version_as_integers[1] == 9:
    version_as_integers[2] = 0
    version_as_integers[1] += 1
elif version_as_integers[2] == 9 and version_as_integers[1] == 9:
    version_as_integers[2] = 0
    version_as_integers[1] = 0
    version_as_integers[0] += 1

version_as_string = [str(el_1) for el_1 in version_as_integers]
print(".".join(version_as_string))
