#Calcular altura y profundidad:
#8.    Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
#hasta una hoja).
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def altura_arbol(nodo):
    """
    Calcula la altura del árbol.
    
    :param nodo: Nodo raíz del árbol.
    :return: La altura del árbol.
    """
    if nodo is None:
        return 0
    else:
        # Calcula la altura del subárbol izquierdo
        altura_izquierda = altura_arbol(nodo.izquierdo)
        # Calcula la altura del subárbol derecho
        altura_derecha = altura_arbol(nodo.derecho)
        # La altura del árbol es el máximo de las alturas de los subárboles más uno
        return max(altura_izquierda, altura_derecha) + 1

# Ejemplo de uso
nodo_raiz = Nodo(1)
nodo_raiz.izquierdo = Nodo(2)
nodo_raiz.derecho = Nodo(3)
nodo_raiz.izquierdo.izquierdo = Nodo(4)
nodo_raiz.izquierdo.derecho = Nodo(5)

altura = altura_arbol(nodo_raiz)
print(f"La altura del árbol es {altura}.")
