# polymorphism_demo.py
import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """This method should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates area of a circle."""
        return math.pi * (self.radius ** 2)
