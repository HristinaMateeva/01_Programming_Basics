number_men = int(input())
number_women = int(input())
max_available_tables = int(input())
available_tables_left = True
combinations_counter = 0

for men in range(1, number_men + 1):
    for women in range(1, number_women + 1):
        combinations_counter += 1
        if max_available_tables < combinations_counter:
            available_tables_left = False
            break
        print(f"({men} <-> {women})",end = " ")
