"""Pruebas unitarias para el Repository (TurnoRepositoryCola)."""

import pytest

from repositorio.turno_repository import TurnoRepositoryCola


def test_repositorio_nuevo_esta_vacio():
    repo = TurnoRepositoryCola()
    assert repo.esta_vacio() is True
    assert repo.cantidad_turnos() == 0


def test_agregar_turno_asigna_numeros_consecutivos():
    repo = TurnoRepositoryCola()
    turno1 = repo.agregar_turno("Ana")
    turno2 = repo.agregar_turno("Luis")

    assert turno1.numero == 1
    assert turno2.numero == 2
    assert repo.cantidad_turnos() == 2


def test_atender_siguiente_respeta_el_orden_fifo():
    repo = TurnoRepositoryCola()
    repo.agregar_turno("Ana")
    repo.agregar_turno("Luis")

    primero_atendido = repo.atender_siguiente()

    assert primero_atendido.cliente == "Ana"
    assert repo.cantidad_turnos() == 1


def test_ver_siguiente_no_elimina_el_turno():
    repo = TurnoRepositoryCola()
    repo.agregar_turno("Ana")

    siguiente = repo.ver_siguiente()

    assert siguiente.cliente == "Ana"
    assert repo.cantidad_turnos() == 1  # sigue estando pendiente


def test_atender_siguiente_con_repositorio_vacio_lanza_error():
    repo = TurnoRepositoryCola()
    with pytest.raises(IndexError):
        repo.atender_siguiente()
