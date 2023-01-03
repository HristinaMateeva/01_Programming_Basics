from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, h, side):
        self.h = h
        self.side = side

    def calculate_area(self):
        print("Calculating triangle area...")


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        print("Calculating Circle area...")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        print("Calculating Rectangle area...")


shapes = [Triangle(5, 2), Circle(5), Triangle(8, 9), Triangle(8, 9), Rectangle(2, 4)]

for shape in shapes:
    shape.calculate_area()
