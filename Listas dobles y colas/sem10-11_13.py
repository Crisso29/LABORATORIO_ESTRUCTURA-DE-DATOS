#Comprobar palíndromos:
#13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
class Pila:
    def __init__(self):
        self.items = []
    def esta_vacia(self):
        return self.items == []
    def apilar(self, item):
        self.items.append(item)
    def desapilar(self):
        return self.items.pop()

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  # Convertir la palabra a minúsculas y eliminar espacios en blanco
    pila = Pila()
    # Apilar la mitad de los caracteres en la pila
    for caracter in palabra[:len(palabra) // 2]:
        pila.apilar(caracter)
    # Comparar los caracteres desapilados con la segunda mitad de la palabra
    for caracter in palabra[len(palabra) // 2 + len(palabra) % 2:]:
        if caracter != pila.desapilar():
            return False
    return True

# Ejemplos de uso
palabra1 = "anita lava la tina"
palabra2 = "oso"
palabra3 = "python"

print("¿'{}' es un palíndromo?".format(palabra1), es_palindromo(palabra1))
print("¿'{}' es un palíndromo?".format(palabra2), es_palindromo(palabra2))
print("¿'{}' es un palíndromo?".format(palabra3), es_palindromo(palabra3))
