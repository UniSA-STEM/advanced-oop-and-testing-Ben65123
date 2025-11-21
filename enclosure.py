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
#Allowed animal category, a size limit, cleaniness level starting from 100 and a list of animals currently
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
