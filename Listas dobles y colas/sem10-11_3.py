#Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la
#lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            if posicion == 0:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo_nodo
                self.cabeza = nuevo_nodo
            else:
                actual = self.cabeza
                for _ in range(posicion - 1):
                    actual = actual.siguiente
                    if not actual:
                        return  # No se puede insertar en una posición fuera del rango actual de la lista
                siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                nuevo_nodo.anterior = actual
                nuevo_nodo.siguiente = siguiente
                if siguiente:
                    siguiente.anterior = nuevo_nodo
                else:
                    self.cola = nuevo_nodo

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

# Insertar nodos iniciales
for i in range(1, 6):
    lista.insertar(i, i - 1)

# Insertar un nuevo nodo en la posición 3 con el dato 15
lista.insertar(15, 2)

# Imprimir la lista hacia adelante y hacia atrás
print("Hacia adelante:")
lista.imprimir_adelante()
print("Hacia atrás:")
lista.imprimir_atras()
