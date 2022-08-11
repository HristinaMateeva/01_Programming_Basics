path_of_file = input().split("\\")

required_string = path_of_file[-1].split(".")
print(f"File name: {required_string[0]}")
print(f"File extension: {required_string[1]}")
