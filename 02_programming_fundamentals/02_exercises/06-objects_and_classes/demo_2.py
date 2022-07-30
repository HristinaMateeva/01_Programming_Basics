class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"I am a cat {self.name}"


class Owner:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def take_animal(self, animal):
        self.animals.append(animal)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"I am a dog {self.name}"


cat = Cat("Sharo", 5)
cat_2 = Cat("Lady", 9)
dog = Dog("Oras", 8)

owner = Owner("Ines")
owner_2 = Owner("Mimi")

print(owner.animals)
print(owner_2.animals)

owner.take_animal(cat)
owner.take_animal(dog)
owner_2.take_animal(cat_2)

print(owner.animals[0].name)
print(owner_2.animals)
