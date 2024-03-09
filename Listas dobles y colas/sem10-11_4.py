#Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando
#solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_duplicados(self):
        valores = set()
        actual = self.cabeza
        while actual:
            if actual.dato in valores:
                siguiente = actual.siguiente
                self.eliminar_nodo(actual)
                actual = siguiente
            else:
                valores.add(actual.dato)
                actual = actual.siguiente

    def eliminar_nodo(self, nodo):
        if nodo == self.cabeza:
            self.cabeza = nodo.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
        elif nodo == self.cola:
            self.cola = nodo.anterior
            self.cola.siguiente = None
        else:
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()

# Crear la lista
lista = ListaEnlazada()

# Insertar nodos con datos duplicados
datos = [1, 2, 3, 4, 2, 3, 5, 1]
for dato in datos:
    lista.insertar(dato)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista hacia adelante y hacia atrás
print("Hacia adelante:")
lista.imprimir_adelante()
print("Hacia atrás:")
lista.imprimir_atras()
