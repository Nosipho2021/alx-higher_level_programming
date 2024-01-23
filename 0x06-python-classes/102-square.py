#!/usr/bin/python3
"""
Module containing the Square class definition
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        __init__: Initializes a new instance of the Square class with size.
        area: Returns the area of the square.
        size: Getter method to retrieve the size.
        size: Setter method to set the size with type and value validation.
        __eq__: Overrides the equality operator (==) for comparing square areas.
        __ne__: Overrides the inequality operator (!=) for comparing square areas.
        __gt__: Overrides the greater than operator (>) for comparing square areas.
        __ge__: Overrides the greater than or equal to operator (>=) for comparing square areas.
        __lt__: Overrides the less than operator (<) for comparing square areas.
        __le__: Overrides the less than or equal to operator (<=) for comparing square areas.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class with size.

        Args:
            size (float or int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.

        Args:
            value: The new size value.
        
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Overrides the equality operator (==) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Overrides the greater than operator (>) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Overrides the greater than or equal to operator (>=) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Overrides the less than operator (<) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Overrides the less than or equal to operator (<=) for comparing square areas.

        Args:
            other (Square): The other Square object.

        Returns:
            bool: True if the area is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

