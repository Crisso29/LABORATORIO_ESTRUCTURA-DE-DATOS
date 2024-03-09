#1 DUPLICAR NODOS
class Nodo:
    def __init__(self, dato):
        self.dato=dato  #* El dato que almacena el nodo
        self.siguiente=None  #? Puntero al nodo siguiente
        self.anterior=None  # ? Puntero al nodo anterior

class ListaEnlazadaDoble:
    def __init__(self):
        self.inicio=None  #* Puntero al primer nodo de la lista
        self.final=None  #* Puntero al último nodo de la lista

    def agregar_nodo(self, dato):
        nuevo_nodo=Nodo(dato)  #* Creamos un nuevo nodo con el dato proporcionado
        if not self.inicio:  #! Si la lista está vacía
            self.inicio=nuevo_nodo
            self.final=nuevo_nodo
        else:  #! Si la lista no está vacía
            self.final.siguiente=nuevo_nodo
            nuevo_nodo.anterior=self.final
            self.final=nuevo_nodo  #* Actualizamos la cola de la lista
    def duplicar_nodos(self):
        nodo_actual=self.inicio
        while nodo_actual:  #* Recorremos toda la lista desde el inicio
            nuevo_nodo=Nodo(nodo_actual.dato)
            siguiente_nodo=nodo_actual.siguiente
            nodo_actual.siguiente=nuevo_nodo
            nuevo_nodo.anterior=nodo_actual
            nuevo_nodo.siguiente=siguiente_nodo
            if siguiente_nodo:
                siguiente_nodo.anterior=nuevo_nodo
            nodo_actual=siguiente_nodo
    def imprimir_adelante(self):
        nodo_actual=self.inicio #!Recorre desde al incio hasta el final
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual=nodo_actual.siguiente
        print()
    def imprimir_atras(self):
        nodo_actual=self.final #! Recorre desde el final hacia el inicio
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual = nodo_actual.anterior
        print()

lista=ListaEnlazadaDoble()
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)

print("Lista original hacia adelante:")
lista.imprimir_adelante()
print("Lista original hacia atrás:")
lista.imprimir_atras()

lista.duplicar_nodos()

print("Lista duplicada hacia adelante:")
lista.imprimir_adelante()
print("Lista duplicada hacia atrás:")
lista.imprimir_atras()