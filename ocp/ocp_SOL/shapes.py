"""
Open/Closed Principle (OCP) — Refactorización de ocp.shapes

POR QUÉ se refactorizó:
    En ocp/shapes.py, la clase Shape usa shape_type y cadenas if/elif para
    calcular el área. Cada nueva figura (triángulo, elipse) obliga a modificar
    Shape.calculate_area(): la clase no está cerrada a cambios.

CÓMO se aplica OCP:
    1. Shape es una clase abstracta con calculate_area() abstracto.
    2. Cada figura concreta (Rectangle, Circle) extiende Shape sin tocar el código
       existente de otras figuras.
    3. AreaCalculator depende de Shape, no de tipos concretos: abierto a extensión,
       cerrado a modificación.

RESULTADO:
    Añadir Triangle solo requiere una nueva subclase de Shape, sin editar Rectangle,
    Circle ni AreaCalculator.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstracción estable: extensible sin modificar esta clase."""

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius ** 2


class AreaCalculator:
    """Cliente cerrado a modificación: suma áreas de cualquier Shape futuro."""

    @staticmethod
    def total_area(shapes: list[Shape]) -> float:
        return sum(shape.calculate_area() for shape in shapes)
