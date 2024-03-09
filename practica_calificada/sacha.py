"PREGUNTA 2"
#* Diseña un algoritmo que determine si dos árboles binarios son idénticos, es decir, si tienen la misma estructura y
#* contienen los mismos valores en nodos correspondientes.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

def son_arboles_identicos(arbol1, arbol2):
    #Si ambos árboles son nulos, son idénticos
    if arbol1 is None and arbol2 is None:
        return True
    
    # Si solo uno de los árboles es nulo, no son idénticos
    if arbol1 is None or arbol2 is None:
        return False
    
    # Compara los datos de los nodos actuales
    if arbol1.dato != arbol2.dato:
        return False
    
    # Compara recursivamente las subárboles izquierdo y derecho
    return (son_arboles_identicos(arbol1.izquierda, arbol2.izquierda) and
            son_arboles_identicos(arbol1.derecha, arbol2.derecha))

# Ejemplo de uso
# Creamos los árboles
arbol1 = Nodo(1)
arbol1.izquierda = Nodo(2)
arbol1.derecha = Nodo(3)
arbol1.izquierda.izquierda = Nodo(4)
arbol1.izquierda.derecha = Nodo(5)

arbol2 = Nodo(1)
arbol2.izquierda = Nodo(2)
arbol2.derecha = Nodo(3)
arbol2.izquierda.izquierda = Nodo(4)
arbol2.izquierda.derecha = Nodo(5)

# Comprobamos si son idénticos
if son_arboles_identicos(arbol1, arbol2):
    print("Los árboles son idénticos.")
else:
    print("Los árboles no son idénticos.")
