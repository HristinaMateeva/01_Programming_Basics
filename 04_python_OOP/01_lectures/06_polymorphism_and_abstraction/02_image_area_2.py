class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __len__(self, other):
        return self.get_area() <= other.get_area()


# ------------------------------
# test code is the same as 02_image_area
