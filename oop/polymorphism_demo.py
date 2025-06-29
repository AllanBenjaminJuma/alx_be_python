import math

class Shape:
    """
    Base class for geometric shapes.
    Defines an area() method that must be overridden by subclasses.
    """
    def area(self):
        """
        Calculates the area of the shape. This method should be
        overridden by concrete shape classes.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")


class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.
    Calculates its area based on length and width.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of a rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.
    Calculates its area based on its radius.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of a circle.
        Uses math.pi for the value of pi.
        """
        return math.pi * (self.radius ** 2)