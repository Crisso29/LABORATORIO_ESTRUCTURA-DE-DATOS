class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.largo =  0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.largo ==  0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.proximo:
                actual = actual.proximo
            actual.proximo = nodo
        self.largo +=  1

    def concatenar(self, lista2):
        if self.largo ==  0:
            self.primero = lista2.primero
        else:
            actual = self.primero
            while actual.proximo:
                actual = actual.proximo
            actual.proximo = lista2.primero
        self.largo += lista2.largo

def principal():
    lista1 = ListaEnlazada()
    lista1.agregar(1)
    lista1.agregar(2)
    lista1.agregar(3)

    lista2 = ListaEnlazada()
    lista2.agregar(4)
    lista2.agregar(5)
    lista2.agregar(6)

    lista1.concatenar(lista2)

    actual = lista1.primero
    while actual:
        print(actual.valor)
        actual = actual.proximo

if __name__ == "__main__":
    principal()