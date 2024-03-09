#Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato
#impar e imprime la lista hacia adelante y hacia atrás.

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
    def contar_pares_impares(self):
        nodo_actual=self.inicio
        pares=0
        impares=0
        while nodo_actual:
            if nodo_actual.dato % 2 ==0:
                pares += 1
            else:
                impares += 1
            nodo_actual = nodo_actual.siguiente
        return pares, impares
    
    def imprimir_adelante(self):
        nodo_actual=self.inicio
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual=nodo_actual.siguiente
        print()
    def imprimir_atras(self):
        nodo_actual=self.final
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual=nodo_actual.anterior
        print()

lista = ListaEnlazadaDoble()
for i in range(1, 10):
    lista.agregar_nodo(i)


pares, impares = lista.contar_pares_impares()
print("Cantidad de nodos con dato par:", pares)
print("Cantidad de nodos con dato impar:", impares)


print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()