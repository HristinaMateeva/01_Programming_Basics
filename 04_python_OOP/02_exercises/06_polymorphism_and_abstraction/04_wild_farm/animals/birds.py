from animals.animal import Bird
from food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
