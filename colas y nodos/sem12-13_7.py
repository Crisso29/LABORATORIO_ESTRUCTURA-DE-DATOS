
#7.     Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo). 
def contar_nodos_internos(nodo):
    """
    Cuenta la cantidad de nodos internos en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos internos en el árbol.
    """
    if nodo is None:
        return 0
    elif nodo.get('hijos', []): # Si el nodo tiene al menos un hijo
        return 1 + sum(contar_nodos_internos(hijo) for hijo in nodo['hijos'])
    else:
        return 0

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo interno
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo interno
    ]
}

cantidad_nodos_internos = contar_nodos_internos(arbol)
print(f"El árbol tiene {cantidad_nodos_internos} nodos internos.")
