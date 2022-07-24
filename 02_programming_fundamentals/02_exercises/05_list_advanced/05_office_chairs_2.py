rooms = int(input())

free_chairs = 0
enough_space = True

for num in range(1, rooms + 1):
    available_chairs, taken_chairs = input().split()
    if len(available_chairs) > int(taken_chairs):
        free_chairs += len(available_chairs) - int(taken_chairs)
    elif len(available_chairs) < int(taken_chairs):
        free_chairs = 0
        needed_chairs = int(taken_chairs) - len(available_chairs)
        enough_space = False
        print(f"{needed_chairs} more chairs needed in room {num}")
if enough_space:
    print(f"Game On, {free_chairs} free chairs left")
