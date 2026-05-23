# SRP — Single Responsibility Principle

## Código original (`srp/file_manager.py`)

`FileManager` implementa `read`, `write`, `compress` y `decompress` en una sola clase.

## Violación detectada

| Responsabilidad | Motivo de cambio |
|-----------------|------------------|
| I/O texto | Cambio de encoding, streaming |
| Compresión ZIP | Otro formato (tar.gz, 7z) |
| Extracción | Destino, validación, seguridad |

Una clase con cuatro motivos de cambio viola SRP.

## Refactorización (`srp_SOL/file_manager.py`)

| Clase | Responsabilidad única |
|-------|----------------------|
| `FileReader` | Leer archivos |
| `FileWriter` | Escribir archivos |
| `FileCompressor` | Comprimir/descomprimir |
| `FileManager` | Delegar (fachada), no implementar todo |

## Cómo se aplica el patrón

- **Antes**: una clase, múltiples responsabilidades acopladas.
- **Después**: cada responsabilidad en su clase; cambios aislados.

## Beneficios/argumento

Si mañana se usa `gzip` en lugar de ZIP, solo cambia `FileCompressor`. `FileReader` y `FileWriter` permanecen intactos.

## Uso

```python
from srp_SOL import FileManager, FileReader, FileWriter

# Uso granular (SRP puro)
FileWriter("nota.txt").write("hola")
print(FileReader("nota.txt").read())

# O fachada compatible con la API original
fm = FileManager("nota.txt")
fm.write("hola")
print(fm.read())
```
