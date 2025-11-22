'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

#Enclosure class for all animals and zoo system. Each enclosure has its own name, environment type,
#Allowed animal category, a size limit, cleanliness level starting from 100 and a list of animals currently
#inside the enclosure.


class Enclosure:
    def __init__(self, name: str, environment_type: str, allowed_category: str,
                 size: int, cleanliness: int = 100):
        if not name:
            raise ValueError("Enclosure name cannot be empty.")
        if not environment_type:
            raise ValueError("Environment type cannot be empty.")
        if not allowed_category:
            raise ValueError("Allowed category cannot be empty.")
        if size <= 0:
            raise ValueError("Enclosure size must be greater than 0.")
        if cleanliness < 0 or cleanliness > 100:
            raise ValueError("Cleanliness must be between 0 and 100.")

        self.__name = name
        self.__environment_type = environment_type
        self.__allowed_category = allowed_category
        self.__size = size
        self.__cleanliness = cleanliness
        self.__animals = []

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not name:
            raise ValueError("Enclosure name cannot be empty.")
        self.__name = name


    def get_environment_type(self):
        return self.__environment_type

    def set_environment_type(self, environment_type: str):
        if not environment_type:
            raise ValueError("Environment type cannot be empty.")
        self.__environment_type = environment_type


    def get_allowed_category(self):
        return self.__allowed_category

    def set_allowed_category(self, allowed_category: str):
        if not allowed_category:
            raise ValueError("Allowed category cannot be empty.")
        self.__allowed_category = allowed_category


    def get_size(self):
        return self.__size

    def set_size(self, size: int):
        if not size:
            raise ValueError("Enclosure size cannot be empty.")
        self.__size = size

    def get_cleanliness(self):
        return self.__cleanliness

    def set_cleanliness(self, cleanliness: int):
        if cleanliness < 0 or cleanliness > 100:
            raise ValueError("Cleanliness must be between 0 and 100.")
        self.__cleanliness = cleanliness

    name = property(get_name, set_name)
    environment_type = property(get_environment_type, set_environment_type)
    allowed_category = property(get_allowed_category, set_allowed_category)
    size = property(get_size, set_size)
    cleanliness = property(get_cleanliness, set_cleanliness)

    #Created add_animals method, checks if animal is of type animal, checks if animal category is allowed in
    #that specific enclosure then lastly checks if the enclosure is full.
    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Only Animal objects can be added to an enclosure.")

        if animal.category != self.allowed_category:
            raise ValueError("This animal cannot be added to this enclosure.")

        if len(self.__animals) >= self.size:
            raise ValueError("Enclosure is full.")

        self.__animals.append(animal)
        return f"Added {animal.name} to the enclosure."

    #removes animal from enclosure.
    def remove_animal(self, animal: Animal):
        if animal not in self.__animals:
            raise ValueError("Animal is not in this enclosure.")
        self.__animals.remove(animal)

    #Clean method enables the cleaning of an enclosure.
    def clean(self):
        self.__cleanliness = 100
        return f"{self.__name} has been cleaned. Cleanliness is now {self.__cleanliness}."

    def __str__(self):
        return (f"Enclosure: {self.__name}, Environment: {self.__environment_type}, "
                f"Allowed category: {self.__allowed_category}, Cleanliness: {self.__cleanliness},")



#tests
# from Zoo_animals import Lion
# enclosure = Enclosure("Savannah Habitat", "Savannah", "Mammal", 2)
# simba = Lion("Simba", 5)
# print(enclosure.add_animal(simba))
# print(enclosure)
# print(enclosure.clean())





