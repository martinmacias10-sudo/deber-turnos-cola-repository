# Sistema de Atención de Turnos (Cola FIFO + Repository)

Proyecto de la actividad **Semana 7: Patrones de diseño, testing unitario y tipos de datos abstractos lineales** — curso Programación Estructurada.

**Autor:** Martín Macías

## Descripción del problema

Se simula un sistema de atención al cliente por turnos (por ejemplo, una ventanilla de banco): los clientes llegan, reciben un número de turno y son atendidos **en el mismo orden en que llegaron**. Este comportamiento corresponde exactamente a una **Cola (Queue)**, un Tipo de Dato Abstracto (TDA) lineal de tipo **FIFO** (*First In, First Out*): el primero en entrar es el primero en salir.

## Estructura de datos implementada

La cola está implementada manualmente en [`estructuras/cola.py`](estructuras/cola.py) usando **nodos enlazados** (sin usar `collections.deque`, `queue.Queue` ni una lista de Python como cola). Se mantienen referencias al frente y al final de la cola para que agregar y eliminar elementos sean operaciones de tiempo constante.

Operaciones implementadas:

| Operación | Método |
|---|---|
| Agregar elemento | `encolar(dato)` |
| Eliminar elemento | `desencolar()` |
| Consultar el siguiente elemento | `ver_frente()` |
| Verificar si está vacía | `esta_vacia()` |
| Consultar cantidad de elementos | `tamano()` |

## Patrón de diseño Repository

El patrón **Repository** se usa para separar el manejo de los datos (la cola) de la lógica de la aplicación:

- **`repositorio/turno_repository.py`**
  - `TurnoRepository`: interfaz abstracta (contrato) con las operaciones de negocio sobre turnos (`agregar_turno`, `atender_siguiente`, `ver_siguiente`, `esta_vacio`, `cantidad_turnos`).
  - `TurnoRepositoryCola`: implementación concreta que usa la `Cola` de `estructuras/cola.py` para almacenar los turnos.
- **`servicios/sistema_atencion.py`**
  - `SistemaAtencion`: contiene la lógica de la aplicación (registrar clientes, atender clientes). Recibe el repositorio por **inyección de dependencia** en su constructor y solo conoce la interfaz `TurnoRepository`, nunca la cola directamente.

Esta separación permite, por ejemplo, cambiar la forma de almacenar los turnos (otra estructura, una base de datos, un archivo) sin tener que modificar `SistemaAtencion`.

## Estructura del proyecto

```
.
├── main.py                          # Script de demostración
├── estructuras/
│   └── cola.py                      # Cola (TDA lineal) implementada manualmente
├── modelos/
│   └── turno.py                     # Modelo de dominio Turno
├── repositorio/
│   └── turno_repository.py          # Patrón Repository (interfaz + implementación)
├── servicios/
│   └── sistema_atencion.py          # Lógica de la aplicación
└── tests/
    ├── test_cola.py                 # Pruebas unitarias de la Cola
    ├── test_turno_repository.py     # Pruebas unitarias del Repository
    └── test_sistema_atencion.py     # Pruebas de integración del servicio
```

## Requisitos

- Python 3.10 o superior
- [pytest](https://docs.pytest.org/) para las pruebas unitarias

## Cómo ejecutar el programa

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

Esto simula el registro de varios clientes y su atención en orden FIFO.

## Cómo ejecutar las pruebas unitarias

1. Instalar pytest (si no lo tienes):

   ```bash
   pip install pytest
   ```

2. Desde la carpeta raíz del proyecto, ejecutar:

   ```bash
   pytest -v
   ```

   Esto ejecuta las 16 pruebas unitarias e imprime el resultado de cada una (`PASSED`/`FAILED`).
