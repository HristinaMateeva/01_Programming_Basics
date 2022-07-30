class Person:
    def __init__(self, hair_color, weight, h):
        self.hair_color = hair_color
        self.weight = weight
        self.height = h

    def sleep(self):
        self.height += 1
        return f"I am sleeping and my height now is {self.height}"


person = Person("blonde", 90, 170)
person_2 = Person("blue", 60, 120)
person_3 = Person("blonde", 70, 200)

print(person.sleep())
print(person.sleep())
print(person_2.sleep())


# class Cat:
#     kind = "mammal"
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat = Cat("Sharo")
# car_2 = Cat("Lady")
