import math

# Base class
class Shape:
    def area(self):
        return 0

# Subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
circle = Circle(5)
print("Area of the circle:", circle.area())

# Example usage 
shape = Shape()
print("Area of the shape:", shape.area())
# Output:
# Area of the circle: 78.53981633974483
# Area of the shape: 0
# The code defines a base class `Shape` with a method `area` that returns 0.
# It also defines a subclass `Circle` that overrides the `area` method to 
# calculate the area of a circle using the formula πr².