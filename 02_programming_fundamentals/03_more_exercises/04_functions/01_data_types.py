line_type = input()
input_data = input()


def data_types(type_data, data):
    if type_data == "int":
        data = int(data)
        return data * 2
    elif type_data == "real":
        data = float(data)
        return f"{(data * 1.5):.2f}"
    else:
        return f"${data}$"


print(data_types(line_type, input_data))
