"""
Interface Segregation Principle (ISP) — Refactorización de isp.printers

POR QUÉ se refactorizó:
    En isp/printers.py, la interfaz Printer obliga a implementar print(), fax() y
    scan(). OldPrinter no soporta fax ni scan y lanza NotImplementedError: el
    cliente queda forzado a depender de métodos que no usa ni puede usar.

CÓMO se aplica ISP:
    1. Se segregan interfaces pequeñas y específicas: IPrintable, IFaxable, IScannable.
    2. Cada clase implementa solo las interfaces que realmente ofrece.
    3. OldPrinter implementa solo IPrintable; ModernPrinter implementa las tres.

RESULTADO:
    Ningún cliente depende de métodos innecesarios. Las interfaces pertenecen
    al cliente que las consume, no a una jerarquía monolítica.
"""

from abc import ABC, abstractmethod


class IPrintable(ABC):
  """Contrato mínimo para imprimir documentos."""

  @abstractmethod
  def print(self, document: str) -> None:
    pass


class IFaxable(ABC):
  """Contrato mínimo para enviar fax."""

  @abstractmethod
  def fax(self, document: str) -> None:
    pass


class IScannable(ABC):
  """Contrato mínimo para escanear documentos."""

  @abstractmethod
  def scan(self, document: str) -> None:
    pass


class OldPrinter(IPrintable):
  """Solo imprime; no está obligada a implementar fax ni scan."""

  def print(self, document: str) -> None:
    print(f"Printing {document} in black and white...")


class ModernPrinter(IPrintable, IFaxable, IScannable):
  """Dispositivo multifunción: implementa solo las interfaces que soporta."""

  def print(self, document: str) -> None:
    print(f"Printing {document} in color...")

  def fax(self, document: str) -> None:
    print(f"Faxing {document}...")

  def scan(self, document: str) -> None:
    print(f"Scanning {document}...")
