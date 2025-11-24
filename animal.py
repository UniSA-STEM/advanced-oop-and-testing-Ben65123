'''
File: animal.py
Description: Animal class for zoo system, stores the key attributes of an animal, allows for the creation
of 1 animal at a time. keeps the data private so that they cant be changed or tampered with from the outside.
Have safe ways to access and update the data with the getters, setters and property's.
Using abstractmethod for make sound because this behaviour is different for every species for example
An dog cannot meow.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''


# Animal class for zoo system, stores the key attributes of an animal, allows for the creation of 1 animal at a time.
# keeps the data private so that they cant be changed or tampered with from the outside. Have safe ways
# to access and update the data with the getters, setters and property's.
# Using abstractmethod for make sound because this behaviour is different for every species for example
# An dog cannot meow.
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, diet: str, category: str):
        # Validation to make sure values are not empty.
        if not name:
            raise ValueError("Animal name cannot be empty.")
        if not species:
            raise ValueError("Animal species cannot be empty.")
        if age < 0:
            raise ValueError("Animal age cannot be negative.")
        if not diet:
            raise ValueError("Animal diet cannot be empty.")
        if not category:
            raise ValueError("Animal category cannot be empty.")
        # Private attributes created.
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__category = category
        self.__health_record = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Animal name cannot be empty.")
        self.__name = name

    def get_species(self):
        return self.__species

    def set_species(self, species):
        if not species:
            raise ValueError("Animal species cannot be empty.")
        self.__species = species

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Animal age cannot be negative.")
        self.__age = age

    def get_diet(self):
        return self.__diet

    def set_diet(self, diet):
        if not diet:
            raise ValueError("Animal diet cannot be empty.")
        self.__diet = diet

    def get_category(self):
        return self.__category

    def set_category(self, category):
        if not category:
            raise ValueError("Animal category cannot be empty.")
        self.__category = category
    # Properties for each attribute.
    name = property(get_name, set_name)
    species = property(get_species, set_species)
    age = property(get_age, set_age)
    diet = property(get_diet, set_diet)
    category = property(get_category, set_category)


    #All basic method of an animal used here.
    def eat(self):
        return f"{self.name} is eating. Diet type: {self.diet}"

    def sleep(self):
        return f"{self.name} is now sleeping."

    @abstractmethod
    def make_sound(self):
        pass

    # Assigns health record to a animal
    def assign_health_record(self, record):
        from health_record import HealthRecord
        if not isinstance(record, HealthRecord):
            raise TypeError("Only HealthRecord objects can be assigned.")
        self.__health_record = record

    # Returns false if animal does not have current health issue and true if it does.
    def has_active_health_issue(self):
        return self.__health_record is not None and self.__health_record.active

    # Gets current health record of an animal.
    def get_health_record(self):
        return self.__health_record



    def __str__(self):
        return f"Animal name: {self.name}, Species: {self.species}, Age: {self.age}, Diet: {self.diet}, Category: {self.category}"




