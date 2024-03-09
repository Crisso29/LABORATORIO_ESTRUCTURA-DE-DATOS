"PREGUNTA 1"
#* Crea una lista doblemente enlazada con al menos 8 nodos
class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
class ListaDoblementeEnlazada:
    def __init__(self):
        self.primer_nodo=None
        self.ultimo_nodo=None

    def agregar_nodo(self, dato):
        nuevo_nodo=Nodo(dato)
        if not self.primer_nodo:
            self.primer_nodo=nuevo_nodo
            self.ultimo_nodo=nuevo_nodo
        else:
            nuevo_nodo.anterior=self.ultimo_nodo
            self.ultimo_nodo.siguiente=nuevo_nodo
            self.ultimo_nodo=nuevo_nodo

    def imprimir_lista(self):
        nodo_actual=self.primer_nodo
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual=nodo_actual.siguiente
        print()
    #* Método para extraer una sublista de una lista original basada en un rango específico de posiciones
    def extraer_sublista(self, inicio, fin):
        sublista=ListaDoblementeEnlazada()
        nodo_actual=self.primer_nodo
        indice=1
        while nodo_actual and indice < inicio:
            nodo_actual=nodo_actual.siguiente
            indice+=1
        
        while nodo_actual and indice <= fin:
            sublista.agregar_nodo(nodo_actual.dato)
            nodo_actual=nodo_actual.siguiente
            indice+=1
        return sublista

#! Crear una lista doblemente enlazada con al menos 8 nodos
lista = ListaDoblementeEnlazada()
for i in range(1, 9):
    lista.agregar_nodo(i)

# Imprimir la lista original
print("Lista original:")
lista.imprimir_lista()

#* Realizar pruebas con diferentes rangos y mostrar las sublistas resultantes
print("\nPruebas de extracción de sublista:")
sublista1 = lista.extraer_sublista(2, 5)
print("Sublista (2-5):")
sublista1.imprimir_lista()

sublista2 = lista.extraer_sublista(3, 7)
print("Sublista (3-7):")
sublista2.imprimir_lista()

sublista3 = lista.extraer_sublista(1, 8)
print("Sublista (1-8):")
sublista3.imprimir_lista()

