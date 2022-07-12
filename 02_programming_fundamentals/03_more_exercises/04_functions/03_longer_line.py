from math import sqrt, pow, floor

coordinate_x1 = float(input())
coordinate_y1 = float(input())
coordinate_x2 = float(input())
coordinate_y2 = float(input())
coordinate_x3 = float(input())
coordinate_y3 = float(input())
coordinate_x4 = float(input())
coordinate_y4 = float(input())


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line_1 = sqrt((pow(x2 - x1, 2)) + (pow(y2 - y1, 2)))
    line_2 = sqrt((pow(x4 - x3, 2)) + (pow(y4 - y3, 2)))
    distance_1 = sqrt(pow(x1, 2) + pow(y1, 2))
    distance_2 = sqrt(pow(x2, 2) + pow(y2, 2))
    distance_3 = sqrt(pow(x3, 2) + pow(y3, 2))
    distance_4 = sqrt(pow(x4, 2) + pow(y4, 2))
    if line_1 >= line_2 and distance_1 < distance_2:
        return f"({coordinate_x1:.0f}, {coordinate_y1:.0f})({coordinate_x2:.0f}, {coordinate_y2:.0f})"
    elif line_1 >= line_2 and distance_1 > distance_2:
        return f"({coordinate_x2:.0f}, {coordinate_y2:.0f})({coordinate_x1:.0f}, {coordinate_y1:.0f})"
    elif line_1 < line_2 and distance_3 < distance_4:
        return f"({coordinate_x3:.0f}, {coordinate_y3:.0f})({coordinate_x4:.0f}, {coordinate_y4:.0f})"
    elif line_1 < line_2 and distance_3 > distance_4:
        return f"({coordinate_x4:.0f}, {coordinate_y4:.0f})({coordinate_x3:.0f}, {coordinate_y3:.0f})"


print(
    longer_line(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2, coordinate_x3, coordinate_y3, coordinate_x4,
                coordinate_y4))

# с math.floor също не се получава (при отрицателна стойност закръгля към по-висока абсолютна стойност)
