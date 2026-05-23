# OCP — Open/Closed Principle

## Código original (`ocp/shapes.py`)

Una sola clase `Shape` con `shape_type` y ramas `if/elif` para rectangle y circle.

## Violación detectada

| Actor | Problema |
|-------|----------|
| `Shape.calculate_area` | Crece con cada nueva figura (modificación) |
| Cohesión | Mezcla datos y lógica de tipos distintos en una clase |
| Riesgo | Cada cambio puede romper figuras ya existentes |

## Refactorización (`ocp_SOL/shapes.py`)

1. **`Shape` (ABC)**: define el contrato `calculate_area()`.
2. **`Rectangle(Shape)`** y **`Circle(Shape)`**: lógica propia encapsulada.
3. **`AreaCalculator`**: opera sobre `Shape`; no conoce tipos concretos.

## Extensión posible sin modificar código existente

```python
class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return self.base * self.height / 2
```

No se toca `Rectangle`, `Circle` ni `AreaCalculator`.

## Cómo se aplica el patrón

- **Antes**: cerrado a extensión limpia, abierto a modificación constante.
- **Después**: abierto a extensión (nuevas subclases), cerrado a modificación del núcleo.

## Uso

```python
from ocp_SOL import AreaCalculator, Circle, Rectangle

shapes = [Rectangle(4, 5), Circle(2)]
print(AreaCalculator.total_area(shapes))
```
