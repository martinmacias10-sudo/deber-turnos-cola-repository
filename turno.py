"""Modelo de dominio: representa un turno de atención."""

from dataclasses import dataclass


@dataclass
class Turno:
    """Un turno asignado a un cliente."""

    numero: int
    cliente: str

    def __str__(self):
        return f"Turno #{self.numero} - {self.cliente}"
