'''
File: main.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

"""
Main demonstration file for the zoo system.
"""

from Zoo_animals import Lion, Elephant
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord

#  Create Animals
simba = Lion("Simba", 5)
dumbo = Elephant("Dumbo", 10)

print("Animals created:")
print(simba)
print(dumbo)
print()

#  Create Enclosures
savannah = Enclosure("Savannah Habitat", "Savannah", "Mammal", 2)
print(f"Created enclosure: {savannah}")
print()

#  Add animals to enclosure
savannah.add_animal(simba)
savannah.add_animal(dumbo)

print("Animals added to enclosure:")
print(savannah)
print()

#  Create Staff
keeper = Zookeeper("Alex", 1)
vet = Veterinarian("Dr. Kim", 2)

print(keeper)
print(vet)
print()

#  Staff Actions
print(keeper.feed_animal(simba))
print(keeper.clean_enclosure(savannah))
print()

#  Health System Demo
print(vet.conduct_health_check(simba, "Injury on paw", "High", "Rest and bandage"))
print(f"Simba active health issue: {simba.has_active_health_issue()}")
print()

#  Try to move animal fail
try:
    new_enclosure = Enclosure("Backup Habitat", "Savannah", "Mammal", 2)
    new_enclosure.add_animal(simba)
except Exception as e:
    print(f"Movement blocked: {e}")
print()

# Vet resolves issue
print(vet.resolve_health_issue(simba))
print(f"Simba active health issue: {simba.has_active_health_issue()}")
print()

#  Try movement again
new_enclosure.add_animal(simba)
print(f"Simba moved successfully to: {new_enclosure.name}")
print()

print("--- Final Zoo Status ---")
print(savannah)
print(new_enclosure)


