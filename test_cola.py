"""Pruebas unitarias para la Cola (TDA lineal implementado manualmente)."""

import pytest

from estructuras.cola import Cola


def test_cola_nueva_esta_vacia():
    cola = Cola()
    assert cola.esta_vacia() is True
    assert cola.tamano() == 0


def test_encolar_agrega_un_elemento():
    cola = Cola()
    cola.encolar("A")
    assert cola.esta_vacia() is False
    assert cola.tamano() == 1


def test_ver_frente_no_elimina_el_elemento():
    cola = Cola()
    cola.encolar("A")
    cola.encolar("B")
    assert cola.ver_frente() == "A"
    # ver_frente no debe cambiar el tamaño ni el orden
    assert cola.tamano() == 2


def test_respeta_el_orden_fifo():
    cola = Cola()
    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    assert cola.desencolar() == "A"
    assert cola.desencolar() == "B"
    assert cola.desencolar() == "C"
    assert cola.esta_vacia() is True


def test_tamano_disminuye_al_desencolar():
    cola = Cola()
    cola.encolar(1)
    cola.encolar(2)
    cola.desencolar()
    assert cola.tamano() == 1


def test_desencolar_con_cola_vacia_lanza_error():
    cola = Cola()
    with pytest.raises(IndexError):
        cola.desencolar()


def test_ver_frente_con_cola_vacia_lanza_error():
    cola = Cola()
    with pytest.raises(IndexError):
        cola.ver_frente()


def test_cola_se_puede_reutilizar_despues_de_vaciarse():
    cola = Cola()
    cola.encolar("A")
    cola.desencolar()
    assert cola.esta_vacia() is True

    # Se puede seguir usando con normalidad después de vaciarse
    cola.encolar("B")
    assert cola.tamano() == 1
    assert cola.ver_frente() == "B"
