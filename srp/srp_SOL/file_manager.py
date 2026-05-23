"""
Single Responsibility Principle (SRP) — Refactorización de srp.file_manager

POR QUÉ se refactorizó:
    En srp/file_manager.py, FileManager lee, escribe, comprime y descomprime.
    Son cuatro razones distintas para cambiar: formato de lectura, política de
    escritura, algoritmo de compresión o destino de extracción. Una sola clase
    concentra responsabilidades no relacionadas.

CÓMO se aplica SRP:
    1. FileReader: solo lectura de archivos de texto.
    2. FileWriter: solo escritura de archivos de texto.
    3. FileCompressor: solo compresión y descompresión ZIP.
    4. FileManager: fachada opcional que delega (compatibilidad de API), sin
       mezclar la lógica interna en un solo cuerpo monolítico.

RESULTADO:
    Cada clase tiene una única responsabilidad y un único motivo de cambio.
"""

from pathlib import Path
from zipfile import ZipFile


class FileReader:
    """Responsabilidad única: leer contenido de un archivo."""

    def __init__(self, filename: str | Path) -> None:
        self.path = Path(filename)

    def read(self, encoding: str = "utf-8") -> str:
        return self.path.read_text(encoding)


class FileWriter:
    """Responsabilidad única: escribir contenido en un archivo."""

    def __init__(self, filename: str | Path) -> None:
        self.path = Path(filename)

    def write(self, data: str, encoding: str = "utf-8") -> None:
        self.path.write_text(data, encoding)


class FileCompressor:
    """Responsabilidad única: comprimir y descomprimir archivos."""

    def __init__(self, filename: str | Path) -> None:
        self.path = Path(filename)

    def compress(self) -> None:
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self) -> None:
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


class FileManager:
    """
    Fachada de conveniencia: delega en clases especializadas.
    Mantiene la misma API pública que srp.file_manager sin violar SRP
    en las clases que realizan el trabajo real.
    """

    def __init__(self, filename: str | Path) -> None:
        self._reader = FileReader(filename)
        self._writer = FileWriter(filename)
        self._compressor = FileCompressor(filename)

    def read(self, encoding: str = "utf-8") -> str:
        return self._reader.read(encoding)

    def write(self, data: str, encoding: str = "utf-8") -> None:
        self._writer.write(data, encoding)

    def compress(self) -> None:
        self._compressor.compress()

    def decompress(self) -> None:
        self._compressor.decompress()
