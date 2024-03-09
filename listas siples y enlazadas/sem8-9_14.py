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

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return
        valores_vistos = set()
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.dato in valores_vistos:
                anterior.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente
# Crear una lista enlazada
lista = ListaEnlazada()

# Insertar algunos nodos con valores duplicados
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.insertar(1)
lista.insertar(4)
lista.insertar(2)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista enlazada sin duplicados
nodo_actual = lista.cabeza
while nodo_actual is not None:
    print(nodo_actual.dato, end=" ")
    nodo_actual = nodo_actual.siguiente