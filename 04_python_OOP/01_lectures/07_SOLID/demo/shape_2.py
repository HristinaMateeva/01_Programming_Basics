from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class ICircleDrawable:
    @staticmethod
    def draw_circle(r):
        print(f"Drawing circle with r {r}")


class IRectangleConsoleDrawable:
    @staticmethod
    def draw_top(n):
        print('-' * n)

    @staticmethod
    def draw_side(n):
        for _ in range(n):
            print("|")

    @staticmethod
    def draw_rectangle( a, b):
        IRectangleConsoleDrawable.draw_top(a)
        IRectangleConsoleDrawable.draw_side(b)
        IRectangleConsoleDrawable.draw_top(a)


class Rectangle(Shape, IRectangleConsoleDrawable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self):
        IRectangleConsoleDrawable.draw_rectangle(self.a, self.b)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def draw(self):
        ICircleDrawable.draw_circle(self.r)


def draw_object(objects):
    for obj in objects:
        obj.draw()


rect = Rectangle(4, 5)
circle = Circle(5)
