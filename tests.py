'''
File: tests.py
Description: This file runs certain tests to ensure that each classes is working properly.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''





import pytest

from Zoo_animals import Lion, Elephant
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian
from health_record import HealthRecord


#Animal Tests

def test_animal_valid_creation():
    lion = Lion("Simba", 5)
    assert lion.name == "Simba"
    assert lion.age == 5
    assert lion.species == "Lion"
    assert lion.category == "Mammal"


def test_animal_invalid_age():
    with pytest.raises(ValueError):
        Lion("Simba", -1)


# Enclosure Tests

def test_add_animal_to_correct_enclosure():
    enclosure = Enclosure("Savannah", "Savannah", "Mammal", 2)
    lion = Lion("Simba", 5)
    enclosure.add_animal(lion)
    # No error means success
    assert True


def test_add_wrong_category_animal_raises():
    enclosure = Enclosure("Reptile House", "Desert", "Reptile", 2)
    lion = Lion("Simba", 5)
    with pytest.raises(ValueError):
        enclosure.add_animal(lion)


#  Health & Movement Tests

def test_health_record_blocks_movement():
    enclosure1 = Enclosure("Savannah", "Savannah", "Mammal", 2)
    enclosure2 = Enclosure("Backup Habitat", "Savannah", "Mammal", 2)
    lion = Lion("Simba", 5)

    enclosure1.add_animal(lion)

    # Assign health record so lion is sick
    record = HealthRecord("Injury", "High", "Rest needed")
    lion.assign_health_record(record)

    with pytest.raises(ValueError):
        enclosure2.add_animal(lion)


def test_resolved_health_allows_movement():
    enclosure1 = Enclosure("Savannah", "Savannah", "Mammal", 2)
    enclosure2 = Enclosure("Backup Habitat", "Savannah", "Mammal", 2)
    lion = Lion("Simba", 5)

    enclosure1.add_animal(lion)

    # Create vet and give treatment
    vet = Veterinarian("Dr. Kim", 1)
    vet.conduct_health_check(lion, "Injury", "High", "Bandaged")
    vet.resolve_health_issue(lion)

    # Should no longer raise
    enclosure2.add_animal(lion)
    assert True


# Staff Action Tests

def test_zookeeper_can_feed():
    keeper = Zookeeper("Alex", 1)
    lion = Lion("Simba", 5)
    result = keeper.feed_animal(lion)
    assert "feeding" in result.lower()


def test_veterinarian_assigns_record():
    vet = Veterinarian("Dr. Kim", 1)
    lion = Lion("Simba", 5)
    vet.conduct_health_check(lion, "Injury", "High", "Treatment started")
    record = lion.get_health_record()
    assert record.issue == "Injury"
    assert lion.has_active_health_issue()
