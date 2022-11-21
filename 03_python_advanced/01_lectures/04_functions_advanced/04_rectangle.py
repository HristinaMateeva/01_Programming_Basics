def rectangle(length, width):
    if not type(length) == int or not type(width) == int:
        return "Enter valid values!"

    def area():
        rectangle_area = length * width
        return rectangle_area

    def perimeter():
        perimeter_rectangle = 2 * (length + width)
        return perimeter_rectangle

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# ------------------------------
print(rectangle(2, 10))
# ------------------------------
print(rectangle('2', 10))
