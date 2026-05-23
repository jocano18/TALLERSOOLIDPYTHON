"""Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies."""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
