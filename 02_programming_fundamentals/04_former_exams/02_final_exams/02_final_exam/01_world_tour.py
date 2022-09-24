def add_stop_command(f_initial_stops, f_command):
    index = int(f_command[1])
    stop_to_add = f_command[2]
    if 0 <= index < len(f_initial_stops):
        left_side = f_initial_stops[:index]
        right_side = f_initial_stops[index:]
        f_initial_stops = left_side + stop_to_add + right_side
    return f_initial_stops


def remove_stop_command(f_initial_stops, f_command):
    start_index = int(f_command[1])
    end_index = int(f_command[2])
    if 0 <= start_index < len(f_initial_stops) and 0 <= end_index < len(f_initial_stops):
        left_side = f_initial_stops[:start_index]
        right_side = f_initial_stops[end_index + 1:]
        f_initial_stops = left_side + right_side
    return f_initial_stops


def switch_command(f_initial_stops, f_command):
    old_stop = f_command[1]
    new_stop = f_command[2]
    if old_stop in f_initial_stops:
        f_initial_stops = initial_stops.replace(old_stop, new_stop)
    return f_initial_stops


initial_stops = input()
command = input()

while not command == "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        initial_stops = add_stop_command(initial_stops, command)
    elif command[0] == "Remove Stop":
        initial_stops = remove_stop_command(initial_stops, command)
    elif command[0] == "Switch":
        initial_stops = switch_command(initial_stops, command)
    print(initial_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {initial_stops}")
