#Ordenar una pila:
#10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

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
    def __len__(self):
        return len(self.items)
def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()  # Creamos una pila auxiliar para ordenar
    while not pila.esta_vacia():
        temp = pila.desapilar()  # Desapilamos un elemento de la pila original
        # Movemos los elementos mayores de la pila auxiliar a la pila original
        while not pila_auxiliar.esta_vacia() and pila_auxiliar.ver_tope() < temp:
            pila.apilar(pila_auxiliar.desapilar())
        # Apilamos el elemento en la posición correcta en la pila auxiliar
        pila_auxiliar.apilar(temp)
    # Movemos los elementos de la pila auxiliar a la pila original para tener el orden ascendente
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())
# Ejemplo de uso
pila = Pila()
elementos = [5, 2, 8, 1, 3]
for elemento in elementos:
    pila.apilar(elemento)

print("Pila original:", pila.items)
ordenar_pila_ascendente(pila)
print("Pila ordenada ascendente:", pila.items)
