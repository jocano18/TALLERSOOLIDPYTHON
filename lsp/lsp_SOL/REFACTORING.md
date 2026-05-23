# LSP — Liskov Substitution Principle

## Código original (`lsp/shapes.py`)

Solo existe `Rectangle` con `width`, `height` y `calculate_area()`.

## Violación típica asociada (anti-patrón que LSP corrige)

```python
# INCORRECTO — viola LSP
class Square(Rectangle):
    def ____________(self, value):
        self.width = self.height = value  # rompe expectativas de Rectangle
```

Si un cliente hace `rect.width = 5; rect.height = 4` esperando área 20, con `Square` obtiene 16.

## Refactorización (`lsp_SOL/shapes.py`)

1. **`Shape` (ABC)**: contrato `calculate_area()` para todos los polígonos.
2. **`Rectangle(Shape)`**: ancho y alto independientes (comportamiento original preservado).
3. **`Square(Shape)`**: hereda de `Shape`, no de `Rectangle`; un solo `side`.
4. **`total_area(shapes)`**: demuestra sustitución: acepta cualquier `Shape`.

## Cómo se aplica el patrón

- **Antes (anti-patrón)**: `Square IS-A Rectangle` con invariantes distintas → no sustituible.
- **Después**: `Rectangle IS-A Shape` y `Square IS-A Shape` con contratos coherentes.

## Beneficios/argumento

Cumple LSP: donde se espera `Shape`, `Rectangle` y `Square` pueden intercambiarse sin alterar la corrección del programa.

## Uso

```python
from lsp_SOL import Rectangle, Square, total_area

figuras = [Rectangle(4, 5), Square(3)]
print(total_area(figuras))  # 20 + 9 = 29
```
