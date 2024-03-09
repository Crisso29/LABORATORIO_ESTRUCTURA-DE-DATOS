class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
def invertir_lista(lista):
    # Inicializando los valores
    prev = None
    curr = lista.cabeza
    nex = curr.siguiente if curr else None

    # Recorriendo la lista y ajustando los punteros
    while curr:
        # Invirtiendo el enlace
        curr.siguiente = prev

        # Moviendo al siguiente nodo
        prev = curr
        curr = nex
        if nex:
            nex = nex.siguiente

    # Inicializando la cabeza de la lista invertida
    lista.cabeza = prev
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def main():
    lista = ListaEnlazada()
    lista.insertar_final(1)
    lista.insertar_final(2)
    lista.insertar_final(3)

    print("Lista original:")
    lista.imprimir_lista()

    invertir_lista(lista)

    print("Lista invertida:")
    lista.imprimir_lista()

if __name__ == "__main__":
    main()