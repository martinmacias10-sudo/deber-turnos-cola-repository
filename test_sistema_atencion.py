"""
Pruebas de integración: el servicio de la aplicación (SistemaAtencion)
usando el Repository real (TurnoRepositoryCola), tal como se usaría
en producción.
"""

from repositorio.turno_repository import TurnoRepositoryCola
from servicios.sistema_atencion import SistemaAtencion


def test_flujo_completo_de_atencion():
    repositorio = TurnoRepositoryCola()
    sistema = SistemaAtencion(repositorio)

    sistema.registrar_cliente("Ana")
    sistema.registrar_cliente("Luis")

    assert sistema.clientes_en_espera() == 2

    mensaje = sistema.atender_cliente()

    assert "Ana" in mensaje
    assert sistema.clientes_en_espera() == 1


def test_atender_cliente_sin_clientes_en_espera():
    repositorio = TurnoRepositoryCola()
    sistema = SistemaAtencion(repositorio)

    mensaje = sistema.atender_cliente()

    assert mensaje == "No hay clientes en espera."


def test_proximo_cliente_no_elimina_el_turno():
    repositorio = TurnoRepositoryCola()
    sistema = SistemaAtencion(repositorio)

    sistema.registrar_cliente("Ana")
    mensaje = sistema.proximo_cliente()

    assert "Ana" in mensaje
    assert sistema.clientes_en_espera() == 1
