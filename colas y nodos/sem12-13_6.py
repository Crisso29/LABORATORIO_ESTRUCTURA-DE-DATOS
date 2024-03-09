#6.    Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).
def contar_nodos_hoja(nodo):
    """
    Cuenta la cantidad de nodos hoja en el árbol.
    
    :param nodo: Diccionario que representa el nodo actual.
    :return: La cantidad total de nodos hoja en el árbol.
    """
    if nodo is None:
        return 0
    elif not nodo.get('hijos', []): # Si el nodo no tiene hijos
        return 1
    else:
        # Suma los nodos hoja de los hijos
        total = 0
        for hijo in nodo.get('hijos', []):
            total += contar_nodos_hoja(hijo)
        return total

# Ejemplo de uso
arbol = {
    'valor': 'A',
    'hijos': [
        {'valor': 'B', 'hijos': [{'valor': 'D'}]}, # Nodo hoja
        {'valor': 'C', 'hijos': [{'valor': 'E'}, {'valor': 'F'}]} # Nodo hoja
    ]
}

cantidad_nodos_hoja = contar_nodos_hoja(arbol)
print(f"El árbol tiene {cantidad_nodos_hoja} nodos hoja.")
