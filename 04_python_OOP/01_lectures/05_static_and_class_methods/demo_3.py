class Person:
   min_age = 0
   max_age = 150

   def __init__(self, name, age):
      self.name = name
      self.age = age

   @classmethod
   def __validate_age(cls, value):
      raise ValueError(f'{value} must be between '
                       f'{cls.min_age} and {cls.max_age}')
# __validate_age() takes the class attributes of class Person
