"""
Implementación manual de una Cola (Queue) genérica.

No se utiliza collections.deque, queue.Queue, ni una lista de Python
usada como cola (list.append/pop). La estructura se construye desde
cero con nodos enlazados, igual que se haría en memoria dinámica en
otros lenguajes (por ejemplo con punteros en C).

Es un Tipo de Dato Abstracto (TDA) lineal de tipo FIFO
(First In, First Out): el primer elemento que entra es el primero
que sale.
"""


class NodoCola:
    """Un nodo individual de la cola: guarda un dato y una referencia
    al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """Cola (FIFO) implementada con nodos enlazados.

    Se mantienen dos referencias: `_frente` (el próximo que sale) y
    `_final` (el último que entró), para que encolar y desencolar
    sean operaciones de tiempo constante O(1).
    """

    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    def encolar(self, dato):
        """Agrega un elemento al final de la cola."""
        nodo_nuevo = NodoCola(dato)
        if self._final is None:
            # La cola estaba vacía: el nuevo nodo es frente y final a la vez.
            self._frente = nodo_nuevo
            self._final = nodo_nuevo
        else:
            self._final.siguiente = nodo_nuevo
            self._final = nodo_nuevo
        self._tamano += 1

    def desencolar(self):
        """Elimina y retorna el elemento que está al frente de la cola."""
        if self.esta_vacia():
            raise IndexError("No se puede desencolar: la cola está vacía")

        nodo_saliente = self._frente
        self._frente = nodo_saliente.siguiente
        if self._frente is None:
            # Ya no quedan nodos: también se limpia la referencia final.
            self._final = None

        self._tamano -= 1
        return nodo_saliente.dato

    def ver_frente(self):
        """Retorna (sin eliminar) el elemento que está al frente de la cola."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía: no hay un elemento al frente")
        return self._frente.dato

    def esta_vacia(self):
        """Retorna True si la cola no tiene elementos."""
        return self._tamano == 0

    def tamano(self):
        """Retorna la cantidad de elementos almacenados en la cola."""
        return self._tamano

    def __len__(self):
        return self._tamano

    def __repr__(self):
        elementos = []
        actual = self._frente
        while actual is not None:
            elementos.append(repr(actual.dato))
            actual = actual.siguiente
        return f"Cola([{', '.join(elementos)}])"
