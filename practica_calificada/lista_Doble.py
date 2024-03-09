"PREGUNTA 3"
#* Crea una lista doblemente enlazada con al menos 10 nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primer_nodo:
            self.primer_nodo = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo_nodo
            self.ultimo_nodo.siguiente = nuevo_nodo
            self.ultimo_nodo = nuevo_nodo

    def imprimir_lista(self):
        nodo_actual = self.primer_nodo
        while nodo_actual:
            print(nodo_actual.dato, end=" ")
            nodo_actual = nodo_actual.siguiente
        print()

    def invertir_en_grupos(self, k):
        if k <= 1 or not self.primer_nodo:
            return
        
        nodo_actual = self.primer_nodo
        while nodo_actual:
            primer_nodo_grupo = nodo_actual
            ultimo_nodo_grupo = primer_nodo_grupo

            # Avanzar k pasos para encontrar el último nodo del grupo
            for _ in range(k - 1):
                if ultimo_nodo_grupo and ultimo_nodo_grupo.siguiente:
                    ultimo_nodo_grupo = ultimo_nodo_grupo.siguiente
                else:
                    break

            # Guardar el nodo siguiente al último nodo del grupo
            siguiente_nodo = ultimo_nodo_grupo.siguiente

            # Invertir los punteros del grupo
            nodo_actual = primer_nodo_grupo
            while nodo_actual != siguiente_nodo:
                nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
                nodo_actual = nodo_actual.anterior

            # Reconectar los grupos invertidos con el resto de la lista
            if primer_nodo_grupo.anterior:
                primer_nodo_grupo.anterior.siguiente = ultimo_nodo_grupo
            else:
                self.primer_nodo = ultimo_nodo_grupo

            if siguiente_nodo:
                siguiente_nodo.anterior = primer_nodo_grupo
            
            primer_nodo_grupo.siguiente = siguiente_nodo
            ultimo_nodo_grupo.anterior = primer_nodo_grupo

            # Avanzar al siguiente grupo
            nodo_actual = siguiente_nodo

# Crear una lista doblemente enlazada con al menos 10 nodos
lista = ListaDoblementeEnlazada()
for i in range(1, 11):
    lista.agregar_nodo(i)

# Imprimir la lista original
print("Lista original:")
lista.imprimir_lista()

# Realizar pruebas con diferentes valores de K
k_values = [2, 3]

for k in k_values:
    print(f"\nInversión en grupos de tamaño {k}:")
    lista.invertir_en_grupos(k)
    lista.imprimir_lista()
