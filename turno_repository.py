"""
Patrón de diseño Repository.

El Repository separa el "cómo se guardan y administran los datos"
(en este caso, en una Cola) de la lógica de la aplicación, que solo
conoce un contrato (una interfaz) y no le importa la estructura
interna usada para almacenar los turnos.

- TurnoRepository: la interfaz (contrato) abstracta.
- TurnoRepositoryCola: la implementación concreta, que usa la Cola
  implementada manualmente en estructuras/cola.py.

Si en el futuro se quisiera cambiar la forma de almacenar los turnos
(por ejemplo, usando una pila, una base de datos, o un archivo), solo
habría que crear una nueva clase que implemente TurnoRepository, sin
tener que modificar el resto de la aplicación (servicios/sistema_atencion.py).
"""

from abc import ABC, abstractmethod

from estructuras.cola import Cola
from modelos.turno import Turno


class TurnoRepository(ABC):
    """Contrato que debe cumplir cualquier repositorio de turnos."""

    @abstractmethod
    def agregar_turno(self, cliente: str) -> Turno:
        """Crea un nuevo turno para `cliente` y lo agrega al almacenamiento."""

    @abstractmethod
    def atender_siguiente(self) -> Turno:
        """Elimina y retorna el turno que debe ser atendido a continuación."""

    @abstractmethod
    def ver_siguiente(self) -> Turno:
        """Retorna (sin eliminar) el turno que sigue en la fila."""

    @abstractmethod
    def esta_vacio(self) -> bool:
        """Indica si no hay turnos pendientes."""

    @abstractmethod
    def cantidad_turnos(self) -> int:
        """Retorna la cantidad de turnos pendientes."""


class TurnoRepositoryCola(TurnoRepository):
    """Implementación concreta del Repository, respaldada por la Cola (FIFO)."""

    def __init__(self):
        self._cola = Cola()
        self._contador = 0

    def agregar_turno(self, cliente: str) -> Turno:
        self._contador += 1
        turno = Turno(numero=self._contador, cliente=cliente)
        self._cola.encolar(turno)
        return turno

    def atender_siguiente(self) -> Turno:
        return self._cola.desencolar()

    def ver_siguiente(self) -> Turno:
        return self._cola.ver_frente()

    def esta_vacio(self) -> bool:
        return self._cola.esta_vacia()

    def cantidad_turnos(self) -> int:
        return self._cola.tamano()
