import os

directory = input()
result = []
extensions = {}

for dir_files in os.walk(directory):
    for file_name in dir_files[2]:
        file = os.path.join(directory, file_name)

        if "." in file:
            extension = file_name.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)

extensions = sorted(extensions.items(), key=lambda x:x[0])

for extension, files in extensions:
    result.append(f".{extension}\n")

    for file in sorted(files):
        result.append(f"- - - {file}\n")

with open("report.txt", "w") as file:
    file.write("".join(result))
