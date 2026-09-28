"""
Lógica de la aplicación (capa de servicio).

SistemaAtencion no sabe nada sobre colas ni nodos: solo conoce la
interfaz TurnoRepository, que recibe por inyección de dependencia en
el constructor. Esto es lo que permite que la lógica de negocio esté
separada del manejo de los datos (el objetivo del patrón Repository).
"""

from repositorio.turno_repository import TurnoRepository


class SistemaAtencion:
    def __init__(self, repositorio: TurnoRepository):
        self._repositorio = repositorio

    def registrar_cliente(self, nombre: str) -> str:
        turno = self._repositorio.agregar_turno(nombre)
        return f"Se registró el turno #{turno.numero} para {nombre}."

    def atender_cliente(self) -> str:
        if self._repositorio.esta_vacio():
            return "No hay clientes en espera."
        turno = self._repositorio.atender_siguiente()
        return f"Atendiendo al turno #{turno.numero}: {turno.cliente}."

    def proximo_cliente(self) -> str:
        if self._repositorio.esta_vacio():
            return "No hay clientes en espera."
        turno = self._repositorio.ver_siguiente()
        return f"El próximo en ser atendido es el turno #{turno.numero}: {turno.cliente}."

    def clientes_en_espera(self) -> int:
        return self._repositorio.cantidad_turnos()
