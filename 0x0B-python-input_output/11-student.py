#!/usr/bin/python3
"""Module defines Student class with methods for JSON serialization and deserialization"""

class Student:


    """Class representing a student"""
    def __init__(self, first_name, last_name, age):


        """Initializes a with first name, last name, and age
        Args: first_name (str): The first name of student
            last_name (str): The last name of student
            age (int): The age of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):


        """Retrieves dictionary representation of a Student instance with attribute filtering
        Args: attrs (list): list of strings specifying the attributes to include (default is None)
        Returns: dict: representation of the Student instance with filtered attributes"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):


        """Replaces all attributes of Student instance based on provided JSON dictionary
         Args:json (dict): representing attributes of Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
