'''
File: staff.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure


class Staff:
    def __init__(self, name: str, role: str, staff_id: int):
        if not name:
            raise ValueError("Staff name cannot be empty.")
        if not role:
            raise ValueError("Staff role cannot be empty.")
        if staff_id <= 0:
            raise ValueError("Staff ID must be greater than 0.")

        self.__name = name
        self.__role = role
        self.__staff_id = staff_id
        self.__assigned_enclosures = []
        self.__assigned_animals = []

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not name:
            raise ValueError("Staff name cannot be empty.")
        self.__name = name

    def get_role(self):
        return self.__role

    def set_role(self, role: str):
        if not role:
            raise ValueError("Staff role cannot be empty.")
        self.__role = role

    def get_staff_id(self):
        return self.__staff_id

    def set_staff_id(self, staff_id: int):
        if staff_id <= 0:
            raise ValueError("Staff ID must be greater than 0.")
        self.__staff_id = staff_id

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    def get_assigned_animals(self):
        return self.__assigned_animals

    name = property(get_name, set_name)
    role = property(get_role, set_role)
    staff_id = property(get_staff_id, set_staff_id)
    assigned_enclosures = property(get_assigned_enclosures)
    assigned_animals = property(get_assigned_animals)


    def assign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Only Enclosure objects can be assigned.")
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)


    def assign_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Only Animal objects can be assigned.")
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)

