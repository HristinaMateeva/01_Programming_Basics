# import os
# # Different unix windows
# absolute_path = os.path.dirname(os.path.abspath(__file__))
#
# file_path = os.path.join(absolute_path, "custom_files", "inner.txt")
# print(file_path)
# file = open(file_path)
# print(file.readlines())

# try:
#     file = open("text.txt")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")

# import os
#
# if os.path.exists("text.txt"):
#     print("File found")
# else:
#     print("File not found")

file = open("example.txt")
print(file.read())