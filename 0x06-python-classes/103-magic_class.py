import math

class MagicClass:
    """
    Represents a MagicClass with radius, area, and circumference calculations.

    Attributes:
        __radius (float): The radius of the MagicClass instance.

    Methods:
        __init__: Initializes a new instance of the MagicClass with a specified radius.
        area: Calculates and returns the area of the MagicClass instance.
        circumference: Calculates and returns the circumference of the MagicClass instance.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass with a specified radius.

        Args:
            radius (float, optional): The radius of the MagicClass instance (default is 0).

        Raises:
            TypeError: If the provided radius is not a number (float or int).
            ValueError: If the provided radius is negative.
        """
        self.__radius = 0  # Default value
        self.radius = radius

    @property
    def radius(self):
        """
        Getter method to retrieve the radius of the MagicClass instance.

        Returns:
            float: The radius of the MagicClass instance.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Setter method to set the radius with type and value validation.

        Args:
            value: The new radius value.

        Raises:
            TypeError: If the radius is not a number (float or int).
            ValueError: If the radius is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        if value < 0:
            raise ValueError("radius must be non-negative")
        self.__radius = value

    def area(self):
        """
        Calculates and returns the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius

