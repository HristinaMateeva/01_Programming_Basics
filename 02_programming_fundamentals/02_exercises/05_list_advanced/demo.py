from math import floor

given_string = input()
given_list = given_string.split(" ")

while True:
    command = input()
    if command == "3:1":
        print(" ".join(given_list[0:]))
        break
    command_list = command.split(" ")
    if command_list[0] == "merge":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        if start_index < 0:
            start_index = 0
        if end_index > (len(given_list) - 1):
            end_index = len(given_list) - 1
        merged_string = "".join(given_list[start_index:(end_index + 1)])
        given_list[start_index:end_index + 1] = [merged_string]
    if command_list[0] == "divide":
        index = int(command_list[1])
        partitions = int(command_list[2])
        chosen_elem = given_list[index]
        partition_length = floor(len(chosen_elem) / partitions)
        partitioned_list = []
        for i in range(0, partitions):
            if i != (partitions - 1):
                partitioned_list.append(chosen_elem[i * partition_length:(i + 1) * partition_length:])
            else:
                partitioned_list.append(chosen_elem[i * partition_length:])
        given_list[index:index + 1] = partitioned_list

