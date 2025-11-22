'''
File: health_record.py
Description: A brief description of this Python module.
Author: Benjamin Sienicki
ID: 110442676
Username: sieby003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    def __init__(self, issue: str, severity: str, treatment_notes: str, active: bool = True):
        if not issue:
            raise ValueError("Health issue cannot be empty.")
        if severity not in ["Low", "Medium", "High"]:
            raise ValueError("Severity must be Low, Medium, or High.")
        if not treatment_notes:
            raise ValueError("Treatment notes cannot be empty.")

        self.__issue = issue
        self.__severity = severity
        self.__treatment_notes = treatment_notes
        self.__active = active

    def get_issue(self):
        return self.__issue

    def set_issue(self, issue: str):
        if not issue:
            raise ValueError("Health issue cannot be empty.")
        self.__issue = issue

    def get_severity(self):
        return self.__severity

    def set_severity(self, severity: str):
        if severity not in ["Low", "Medium", "High"]:
            raise ValueError("Severity must be Low, Medium, or High.")
        self.__severity = severity

    def get_treatment_notes(self):
        return self.__treatment_notes

    def set_treatment_notes(self, notes: str):
        self.__treatment_notes = notes

    def get_active(self):
        return self.__active

    def resolve(self):
        self.__active = False

    issue = property(get_issue, set_issue)
    severity = property(get_severity, set_severity)
    treatment_notes = property(get_treatment_notes, set_treatment_notes)
    active = property(get_active)

    def __str__(self):
        return f"Issue: {self.__issue}, Severity: {self.__severity}, Active: {self.__active}"
