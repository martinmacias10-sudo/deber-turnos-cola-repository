"""
Demostración del sistema de atención de turnos.

Simula una ventanilla de atención al cliente: los clientes llegan,
reciben un turno (se encolan) y son atendidos en el mismo orden en
que llegaron (FIFO), gracias a la Cola implementada manualmente y
administrada a través del Repository.
"""

from repositorio.turno_repository import TurnoRepositoryCola
from servicios.sistema_atencion import SistemaAtencion


def main():
    repositorio = TurnoRepositoryCola()
    sistema = SistemaAtencion(repositorio)

    print("=== Sistema de atención de turnos (Cola / FIFO) ===\n")

    clientes = ["Ana", "Luis", "María", "Carlos"]
    for cliente in clientes:
        print(sistema.registrar_cliente(cliente))

    print(f"\nClientes en espera: {sistema.clientes_en_espera()}")
    print(sistema.proximo_cliente())

    print("\n--- Atendiendo turnos ---")
    while sistema.clientes_en_espera() > 0:
        print(sistema.atender_cliente())

    print("\n--- Intentando atender sin clientes en espera ---")
    print(sistema.atender_cliente())


if __name__ == "__main__":
    main()
