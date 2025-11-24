'''
File: staff.py
Description: Staff class for zoo system. Each staff member has a name, role and staff ID. staff members can be assigned
to different animals and enclosures. Have included 2 types of staff, zookeeper and veterinarian.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''


#Staff class for zoo system. Each staff member has a name, role and staff ID. staff members can be assigned
#to different animals and enclosures. Have included 2 types of staff, zookeeper and veterinarian.

from animal import Animal
from enclosure import Enclosure
from health_record import HealthRecord

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

    # Assigns enclosure to the staff member.
    def assign_enclosure(self, enclosure):
        if not isinstance(enclosure, Enclosure):
            raise TypeError("Only Enclosure objects can be assigned.")
        if enclosure not in self.__assigned_enclosures:
            self.assigned_enclosures.append(enclosure)

    #Assigns animal to the staff.
    def assign_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Only Animal objects can be assigned.")
        if animal not in self.__assigned_animals:
            self.assigned_animals.append(animal)

    def __str__(self):
        return (f"Staff: {self.name}, Role: {self.role}, ID: {self.staff_id}, "
                f"Enclosures: {len(self.assigned_enclosures)}, "
                f"Animals: {len(self.assigned_animals)}")

# #simple tests
# from Zoo_animals import Lion
# from enclosure import Enclosure
# staff = Staff("Alex", "Zookeeper", 1)
# savannah = Enclosure("Savannah Habitat", "Savannah", "Mammal", 3)
# simba = Lion("Simba", 5)
# staff.assign_enclosure(savannah)
# staff.assign_animal(simba)
# print(staff)



class Zookeeper(Staff):
        # Zookeeper is a type of staff that can feed animals and clean enclosures.
        def __init__(self, name: str, staff_id: int):
            super().__init__(name, "Zookeeper", staff_id)

        def feed_animal(self, animal):
            if not isinstance(animal, Animal):
                raise TypeError("Zookeeper can only feed Animal objects.")
            # Call the animal's eat method and return a simple message.
            return f"{self.name} is feeding {animal.name}. {animal.eat()}"

        def clean_enclosure(self, enclosure):
            if not isinstance(enclosure, Enclosure):
                raise TypeError("Zookeeper can only clean Enclosure objects.")
            # Use the enclosure's clean method.
            return  enclosure.clean()

class Veterinarian(Staff):
    # Veterinarian is a staff member that looks after animal health. It can conduct animal health checks and
    # resolve the animals health issue.
    def __init__(self, name: str, staff_id: int):
        super().__init__(name, "Veterinarian", staff_id)

    def conduct_health_check(self, animal, issue: str, severity: str, treatment_notes: str = ""):
        if not isinstance(animal, Animal):
            raise TypeError("Veterinarian can only examine Animal objects.")

        record = HealthRecord(issue, severity, treatment_notes)
        animal.assign_health_record(record)
        return f"{self.name} checked {animal.name} and recorded: {issue} ({severity})."

    def resolve_health_issue(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Veterinarian can only update Animal objects.")

        record = animal.get_health_record()
        record.active = False
        return f"{self.name} has resolved the health issue for {animal.name}."


