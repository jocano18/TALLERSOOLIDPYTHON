# DIP — Dependency Inversion Principle

## Código original (`dip/app.py`)

```python
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end  # depende de concreción

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
```

## Violación detectada

| Actor | Problema |
|-------|----------|
| `FrontEnd` | Depende de la clase concreta `BackEnd`, no de una abstracción |
| Acoplamiento | Alto nivel ligado a bajo nivel; difícil testear y cambiar fuentes |
| Extensibilidad | Añadir `ApiBackEnd` obliga a que `FrontEnd` conozca otro tipo concreto |

## Refactorización (`dip_SOL/app.py`)

1. **`IDataSource` (Protocol)**: abstracción con método `get_data()`.
2. **`FrontEnd`**: recibe `IDataSource` en el constructor; solo llama a `get_data()`.
3. **`BackEnd`**: implementa `get_data()` sin que `FrontEnd` lo importe ni lo nombre.

## Cómo se aplica el patrón

- **Antes**: `FrontEnd → BackEnd` (dependencia directa concreta-concreta).
- **Después**: `FrontEnd → IDataSource ← BackEnd` (ambos dependen de la abstracción).

## Beneficios/argumento

Cumple DIP porque las abstracciones no dependen de detalles; los detalles (`BackEnd`) dependen de la abstracción (`IDataSource`). `FrontEnd` permanece cerrado a cambios en la persistencia.

## Uso

```python
from dip_SOL import BackEnd, FrontEnd

ui = FrontEnd(BackEnd())
ui.display_data()
# Display data: Data from the database
```
