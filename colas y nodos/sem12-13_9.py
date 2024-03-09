
#9.    Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
#hasta el nodo).
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def profundidad_nodo(nodo, valor, profundidad=0):
    """
    Calcula la profundidad de un nodo específico en el árbol.
    
    :param nodo: Nodo raíz del árbol.
    :param valor: Valor del nodo para el cual se quiere calcular la profundidad.
    :param profundidad: Profundidad del nodo actual desde la raíz.
    :return: La profundidad del nodo especificado.
    """
    if nodo is None:
        return -1 # Nodo no encontrado
    if nodo.valor == valor:
        return profundidad # Nodo encontrado, retorna la profundidad
    izquierda = profundidad_nodo(nodo.izquierdo, valor, profundidad + 1)
    if izquierda != -1:
        return izquierda # Si encontramos el nodo en el subárbol izquierdo, retornamos la profundidad
    return profundidad_nodo(nodo.derecho, valor, profundidad + 1) # Buscamos en el subárbol derecho

# Ejemplo de uso
nodo_raiz = Nodo(1)
nodo_raiz.izquierdo = Nodo(2)
nodo_raiz.derecho = Nodo(3)
nodo_raiz.izquierdo.izquierdo = Nodo(4)
nodo_raiz.izquierdo.derecho = Nodo(5)

valor_buscado = 5
profundidad = profundidad_nodo(nodo_raiz, valor_buscado)
if profundidad != -1:
    print(f"La profundidad del nodo con valor {valor_buscado} es {profundidad}.")
else:
    print(f"El nodo con valor {valor_buscado} no se encuentra en el árbol.")