import os
import re

directory = input("Enter a directory: ")
string_to_replace = input("Enter the string that you want to replace: ")
string_to_replace_with = input("Enter the string that you want to replace with: ")

for file_name in os.listdir(directory):
    file = os.path.join(directory, file_name)

    if os.path.isfile(file):
        new_name = file_name.replace(string_to_replace, string_to_replace_with)
        new_file = "/".join(re.split(r"[\\/]", file)[:-1]) + "/" + new_name

        os.rename(file, new_file)