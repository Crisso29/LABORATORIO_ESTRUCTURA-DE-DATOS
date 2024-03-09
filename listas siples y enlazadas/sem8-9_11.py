class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def sumar_valores(self):
        suma =  0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

# Crear una lista enlazada y agregar algunos nodos
lista = ListaEnlazada()
lista.agregar(4)
lista.agregar(2)
lista.agregar(7)

# Sumar los valores de todos los nodos
suma = lista.sumar_valores()
print(suma)  # Esto imprimirá  13