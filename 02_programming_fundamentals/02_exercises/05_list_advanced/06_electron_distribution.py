electrons = int(input())

all_electrons = electrons
shell = []

for num in range(1, electrons + 1):
    current_shell = 2 * (num ** 2)
    electrons -= current_shell
    if electrons == 0:
        shell.append(current_shell)
        break
    elif electrons < 0:
        left_electrons = all_electrons - sum(shell)
        shell.append(left_electrons)
        break
    shell.append(current_shell)

print(shell)
