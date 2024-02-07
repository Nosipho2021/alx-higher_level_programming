#!/usr/bin/python3
"""
Module to create an object from a JSON file
"""

import json

def load_from_json_file(filename):
    """
    Function to create an object from a JSON file

    Args:
        filename (str): The name of the JSON file

    Returns:
        object: The Python data structure represented by the JSON file
    """
    with open(filename, "r") as file:
        return json.load(file)

if __name__ == "__main__":
    # Example usage:
    obj = load_from_json_file("input.json")
    print("Python object:", obj)
