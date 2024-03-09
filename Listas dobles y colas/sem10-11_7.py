#7 CONVERTIR NUMEROS DECIMALES A BINARIOS
class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return len(self.items) == 0
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def decimal_a_binario(decimal):
    pila = Pila()
    while decimal > 0:
        residuo = decimal % 2
        pila.apilar(residuo)
        decimal //= 2
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario if binario else "0"

numero_decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero_decimal)
print("El número decimal", numero_decimal, "en binario es:", binario)
