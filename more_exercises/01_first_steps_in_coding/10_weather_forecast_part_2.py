degrees = float(input())
if 26 <= degrees <= 35:
    print(f"Hot")
elif 20.1 <= degrees <= 25.9:
    print(f"Warm")
elif 15 <= degrees <= 20:
    print(f"Mild")
elif 12 <= degrees <= 14.9:
    print(f"Cool")
elif 5 <= degrees <= 11.9:
    print(f"Cold")
else:
    print("unknown")
