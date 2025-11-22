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