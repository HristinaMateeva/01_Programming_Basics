import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    @staticmethod
    def calc_distance(point_1, point_2):
        return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
