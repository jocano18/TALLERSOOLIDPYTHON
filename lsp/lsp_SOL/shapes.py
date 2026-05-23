"""
Liskov Substitution Principle (LSP) — Refactorización de lsp.shapes

POR QUÉ se refactorizó:
    El ejemplo clásico de violación LSP es Square heredando de Rectangle y
    redefiniendo width/height para mantener lados iguales: un código que espera
    un Rectangle y aumenta solo el ancho deja de calcular bien el área al
    sustituir por Square. lsp/shapes.py solo define Rectangle; la refactorización
    modela el anti-patrón y la corrección explícita.

CÓMO se aplica LSP:
    1. Shape define el contrato común (calculate_area) que cualquier subtipo
       debe cumplir sin alterar el comportamiento esperado.
    2. Rectangle y Square son subtipos independientes de Shape, no Square IS-A
       Rectangle con reglas distintas sobre width/height.
    3. Cualquier función que reciba Shape puede recibir Rectangle o Square sin
       sorpresas: el área siempre refleja las dimensiones reales del objeto.

RESULTADO:
    Los subtipos son sustituibles por su tipo base sin romper la lógica del cliente.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Contrato base: todo subtipo debe calcular área de forma predecible."""

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Rectangle(Shape):
    """Rectángulo con ancho y alto independientes."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Square(Shape):
    """
    Cuadrado como subtipo de Shape, no de Rectangle.
    Evita la violación LSP de forzar width == height en un Rectangle mutable.
    """

    def __init__(self, side: float) -> None:
        self.side = side

    @property
    def width(self) -> float:
        return self.side

    @property
    def height(self) -> float:
        return self.side

    def calculate_area(self) -> float:
        return self.side ** 2


def total_area(shapes: list[Shape]) -> float:
    """Cliente genérico: funciona con cualquier subtipo sustituible de Shape."""
    return sum(shape.calculate_area() for shape in shapes)
