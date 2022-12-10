def forecast(*args):
    forecast_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}
    result = ""
    for arg in args:
        location = arg[0]
        weather = arg[1]
        forecast_dict[weather].append(location)

    for key, values in forecast_dict.items():
        values.sort()
        for value in values:
            result += f"{value} - {key}\n"
    return result


# ------------------------------
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
# ------------------------------
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
# ------------------------------
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
