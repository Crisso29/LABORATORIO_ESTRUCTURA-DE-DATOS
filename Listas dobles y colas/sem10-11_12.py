#Implementar una calculadora sencilla:
#12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar
#expresiones.
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def ver_tope(self):
        return self.items[-1]

def calcular(expresion):
    pila = Pila()
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    elementos = expresion.split()

    for elemento in elementos:
        if elemento.isdigit():  # Si el elemento es un número, lo apilamos
            pila.apilar(float(elemento))
        elif elemento in operadores:  # Si el elemento es un operador, realizamos la operación
            segundo_numero = pila.desapilar()
            primer_numero = pila.desapilar()
            resultado = operadores[elemento](primer_numero, segundo_numero)
            pila.apilar(resultado)

    return pila.desapilar()  # El último elemento en la pila será el resultado

# Ejemplo de uso
expresion = "3 4 + 2 *"
resultado = calcular(expresion)
print("Resultado de la expresión:", resultado)
