#Contar nodos:
#5.    Implementar una función que cuente la cantidad de nodos en el árbol.
def contar_nodos(nodo):
    """    Cuenta la cantidad de nodos en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos en el árbol.
    """
    if nodo is None:
        return 0
    else:
        # Suma 1 para contar el nodo actual
        total = 1
        # Suma los nodos hijos
        for hijo in nodo.get('hijos', []):
            total += contar_nodos(hijo)
        return total

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]},
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]}
    ]
}

cantidad_nodos = contar_nodos(arbol)
print(f"El árbol tiene {cantidad_nodos} nodos.")