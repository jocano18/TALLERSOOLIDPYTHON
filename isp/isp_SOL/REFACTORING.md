# ISP — Interface Segregation Principle

## Código original (`isp/printers.py`)

Una sola interfaz `Printer` con `print`, `fax` y `scan`. `OldPrinter` lanza `NotImplementedError` en fax y scan.

## Violación detectada

| Actor | Problema |
|-------|----------|
| `OldPrinter` | Implementa métodos que no puede cumplir (fax, scan) |
| Clientes | Quien solo imprime depende de una interfaz con fax/scan |
| Mantenimiento | Cambios en scan afectan a impresoras que no escanean |

## Refactorización (`isp_SOL/printers.py`)

1. **`IPrintable`**: solo `print()`.
2. **`IFaxable`**: solo `fax()`.
3. **`IScannable`**: solo `scan()`.
4. **`OldPrinter(IPrintable)`**: una sola responsabilidad de interfaz.
5. **`ModernPrinter(IPrintable, IFaxable, IScannable)`**: composición de interfaces.

## Cómo se aplica el patrón

- **Antes**: interfaz gruesa → clientes dependen de métodos no usados.
- **Después**: interfaces segregadas → cada clase expone solo lo que ofrece.

## Beneficios/argumento

Elimina `NotImplementedError` como señal de diseño incorrecto. Los clientes pueden tipar contra `IPrintable` sin conocer fax ni scan.

## Uso

```python
from isp_SOL import IPrintable, ModernPrinter, OldPrinter

def imprimir(printer: IPrintable, doc: str) -> None:
    printer.print(doc)

imprimir(OldPrinter(), "informe.pdf")
imprimir(ModernPrinter(), "informe.pdf")
```
