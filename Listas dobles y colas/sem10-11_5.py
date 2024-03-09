#Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
#primero y viceversa) e imprime la lista hacia adelante y hacia atrás.
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

    def invertir_lista(self):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            # Intercambiar punteros siguiente y anterior
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
            # Mover al siguiente nodo
            nodo_actual = nodo_actual.anterior

        # Intercambiar los punteros de inicio y final para reflejar el cambio
        self.inicio, self.final = self.final, self.inicio
    def imprimir_hacia_adelante(self):
        nodo_actual = self.inicio
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def imprimir_hacia_atras(self):
        nodo_actual = self.final
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" <- ")
            nodo_actual = nodo_actual.anterior
        print("None")

# Crear la lista enlazada doble
lista = ListaEnlazadaDoble()

# Agregar 6 nodos a la lista
nodos = [1, 2, 3, 4, 5, 6]
for nodo in nodos:
    lista.agregar_nodo(nodo)

# Invertir la lista
lista.invertir_lista()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_hacia_adelante()
print("Lista hacia atrás:")
lista.imprimir_hacia_atras()