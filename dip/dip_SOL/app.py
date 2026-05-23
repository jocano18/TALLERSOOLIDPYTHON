"""
Dependency Inversion Principle (DIP) — Refactorización de dip.app

POR QUÉ se refactorizó:
    En dip/app.py, FrontEnd depende directamente de la clase concreta BackEnd.
    Eso viola DIP: los módulos de alto nivel (FrontEnd) quedan acoplados a los
    detalles de implementación (BackEnd). Si cambiamos la fuente de datos
    (API REST, caché, archivo), debemos modificar FrontEnd.

CÓMO se aplica DIP:
    1. Se introduce IDataSource como abstracción (Protocol) que define el contrato
       get_data() sin revelar de dónde vienen los datos.
    2. FrontEnd recibe cualquier implementación de IDataSource por inyección de
       dependencias; no conoce BackEnd ni otras clases concretas.
    3. BackEnd (y futuras fuentes) dependen de la abstracción al implementarla.

RESULTADO:
    FrontEnd queda estable ante cambios en la capa de datos. Las dependencias
    apuntan hacia abstracciones, no hacia concreciones.
"""

from typing import Protocol


class IDataSource(Protocol):
    """Abstracción: contrato que deben cumplir todas las fuentes de datos."""

    def get_data(self) -> str:
        ...


class FrontEnd:
    """Módulo de alto nivel: depende solo de IDataSource, no de BackEnd."""

    def __init__(self, data_source: IDataSource) -> None:
        self._data_source = data_source

    def display_data(self) -> None:
        data = self._data_source.get_data()
        print("Display data:", data)


class BackEnd:
    """Módulo de bajo nivel: implementa la abstracción (detalle concreto)."""

    def get_data(self) -> str:
        return "Data from the database"
