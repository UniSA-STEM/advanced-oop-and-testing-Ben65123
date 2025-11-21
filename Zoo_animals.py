'''
File: Zoo_animals.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Lion",  age, "Carnivore", "Mammal")

    def make_sound(self):
        return f"{self.name} roars!"

