#8 EVALUAR EXPRESIÓN POSFIJA
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
        

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operandos = expresion.split()
    for elemento in operandos:
        if elemento.isdigit():
            pila.apilar(int(elemento))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if operando1 is None or operando2 is None:
                return "Expresión no válida: no hay suficientes operandos."
            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2
            else:
                return "Expresión no válida: operador no reconocido."
            pila.apilar(resultado)

    if pila.esta_vacia():
        return "Expresión no válida: no hay resultado."
    else:
        return pila.desapilar()

expresion_posfija = input("Ingrese la expresión en notación posfija: ")
resultado = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión es:", resultado)