
#Buscar el mínimo y el máximo:
#10.  Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def nodo_minimo(nodo):
    """
    Encuentra el nodo con el valor mínimo en el árbol.
    
    :param nodo: Nodo raíz del árbol.
    :return: El nodo con el valor mínimo.
    """
    if nodo is None:
        return None
    elif nodo.izquierdo is None:
        return nodo
    else:
        return nodo_minimo(nodo.izquierdo)

# Ejemplo de uso
nodo_raiz = Nodo(50)
nodo_raiz.izquierdo = Nodo(30)
nodo_raiz.derecho = Nodo(70)
nodo_raiz.izquierdo.izquierdo = Nodo(20)
nodo_raiz.izquierdo.derecho = Nodo(40)
nodo_raiz.derecho.izquierdo = Nodo(60)
nodo_raiz.derecho.derecho = Nodo(80)

nodo_min = nodo_minimo(nodo_raiz)
if nodo_min:
    print(f"El nodo con el valor mínimo es {nodo_min.valor}.")
else:
    print("El árbol está vacío.")
