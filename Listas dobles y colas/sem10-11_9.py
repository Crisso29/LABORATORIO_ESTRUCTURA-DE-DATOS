
#Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila.
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

def verificar_anidacion_expresion(expresion):
    pila = Pila()
    for caracter in expresion:
        if caracter in '({[':
            pila.apilar(caracter)
        elif caracter in ')}]':
            if pila.esta_vacia():
                return False
            elemento_tope = pila.desapilar()
            if (caracter == ')' and elemento_tope != '(') or \
               (caracter == '}' and elemento_tope != '{') or \
               (caracter == ']' and elemento_tope != '['):
                return False
    return pila.esta_vacia()

expresion = input("Ingrese una expresión matemática: ")
if verificar_anidacion_expresion(expresion):
    print("Los operadores en la expresión están correctamente anidados.")
else:
    print("Los operadores en la expresión no están correctamente anidados.")