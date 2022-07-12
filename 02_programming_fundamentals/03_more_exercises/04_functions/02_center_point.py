from math import sqrt, pow, floor

coordinate_x1 = float(input())
coordinate_y1 = float(input())
coordinate_x2 = float(input())
coordinate_y2 = float(input())


def center_point(x1, y1, x2, y2):
    diagonal_1 = sqrt(pow(x1, 2) + pow(y1, 2))
    diagonal_2 = sqrt(pow(x2, 2) + pow(y2, 2))
    if diagonal_2 < diagonal_1:
        return f"({floor(x2)}, {floor(y2)})"
    return f"({floor(x1)}, {floor(y1)})"


print(center_point(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2))
