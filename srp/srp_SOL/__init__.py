"""Paquete srp_SOL — Single Responsibility Principle."""

from .file_manager import (
    FileCompressor,
    FileManager,
    FileReader,
    FileWriter,
)

__all__ = ["FileCompressor", "FileManager", "FileReader", "FileWriter"]
