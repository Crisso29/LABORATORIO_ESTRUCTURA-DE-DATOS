class Nodo:
    def __init__(self, dato):
        self.dato=dato
        self.siguiente= None
        self.anterior=None
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza=None
        self.cola=None

    def insertar_nodo(self, dato):
        nuevo_nodo=Nodo(dato)
        if not self.cabeza:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.anterior=self.cola
            self.cola.siguiente=nuevo_nodo
            self.cola=nuevo_nodo

    def imprimir(self):
        actual=self.cabeza
        while actual:
            print(actual.dato, end="->")
            actual=actual.siguiente
        print(None)

    def transferir(self, otra_cuenta, cantidad):
        if self.cola and otra_cuenta.cola:
            if self.cola.dato>=cantidad:
                self.cola.dato-=cantidad
                otra_cuenta.cola.dato+=cantidad
                print(f"Transferencia exitosa de {cantidad} unidades de cuenta A a cuenta B")
            else:
                print("Fondos insuficientes en cuenta A para realizar la transferencia")
        else:
            print("Una de las cuentas o ambas cuentas están vacías")

cuenta_A=ListaDobleEnlazada()
cuenta_B=ListaDobleEnlazada()

cuenta_A.insertar_nodo(300)
cuenta_B.insertar_nodo(200)

#*Imprimir el estado inicial
print("Estado inicia de las cuentas: ")
print(f" La cuenta A tiene: ")
cuenta_A.imprimir()
print(f" La cuenta B tiene: ")
cuenta_B.imprimir()

#*Realizar varias operaciones transacionales 
cuenta_A.transferir(cuenta_B, 20)
cuenta_B.transferir(cuenta_B, 10)


print("Cuenta A: ")
cuenta_A.imprimir()
print("cuenta B: ")
cuenta_B.imprimir()
