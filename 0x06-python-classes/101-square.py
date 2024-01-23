#!/usr/bin/python3
"""
Module containing the Square class definition
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__: Initializes a new instance of the Square class with optional size and position.
        area: Returns the area of the square.
        size: Getter method to retrieve the size.
        size: Setter method to set the size with type and value validation.
        position: Getter method to retrieve the position.
        position: Setter method to set the position with type and value validation.
        my_print: Prints the square using '#' characters with respect to the position.
        __str__: Returns a string representation of the square, same as my_print().
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class with optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with type and value validation.

        Args:
            value: The new size value.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position with type and value validation.

        Args:
            value (tuple): The new position value.
        
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters with respect to the position.
        If size is equal to 0, prints an empty line.
        Position is used by adding space before printing '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square, same as my_print().

        Returns:
            str: The string representation of the square.
        """
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()

