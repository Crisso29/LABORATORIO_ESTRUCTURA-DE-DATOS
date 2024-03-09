class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def longitud(self):
        nodo_actual = self.cabeza
        longitud = 0
        while nodo_actual is not None:
            longitud += 1
            nodo_actual = nodo_actual.siguiente
        return longitud
# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar algunos nodos
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(4)
lista.insertar(5)

# Obtener la longitud de la lista enlazada
longitud = lista.longitud()
print(f"La longitud de la lista enlazada es: {longitud}")