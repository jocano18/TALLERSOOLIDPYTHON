"""Paquete isp_SOL — Interface Segregation Principle."""

from .printers import (
    IFaxable,
    IPrintable,
    IScannable,
    ModernPrinter,
    OldPrinter,
)

__all__ = [
    "IFaxable",
    "IPrintable",
    "IScannable",
    "ModernPrinter",
    "OldPrinter",
]
