'''
File: Zoo_animals.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
#Animals for zoo created. Each subclass is a different animal with species, diet and category automatically
#stored already, while name and age is required to be entered by user. Each subclass overrides the make_sound
#method created in the animals file as this was a abstract method.
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Lion",  age, "Carnivore", "Mammal")

    def make_sound(self):
        return f"{self.name} roars!"

class Giraffe (Animal):
    def __init__(self, name, age):
        super().__init__(name, "Giraffe",  age, "Herbivore", "Mammal")

    def make_sound(self):
        return f"{self.name} makes humming sounds"

class Snake(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Snake", age, "Carnivore", "Reptile")

    def make_sound(self):
        return f"{self.name} hissessss."

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Elephant", age, "Herbivore", "Mammal")

    def make_sound(self):
        return f"{self.name} trumpets!"

class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Zebra", age, "Herbivore", "Mammal")

    def make_sound(self):
        return f"{self.name} whinnies."



