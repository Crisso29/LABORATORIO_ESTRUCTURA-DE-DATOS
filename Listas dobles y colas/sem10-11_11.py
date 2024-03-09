def eliminar_duplicados_pila(pila):
    # Crear una nueva lista para almacenar los elementos únicos
    pila_sin_duplicados = []
    
    # Iterar sobre los elementos de la pila original
    for elemento in pila:
        # Si el elemento no está en la nueva pila, agregarlo
        if elemento not in pila_sin_duplicados:
            pila_sin_duplicados.append(elemento)
    
    # Devolver la nueva pila sin duplicados
    return pila_sin_duplicados

# Ejemplo de uso
pila_original = [1,  2,  3,  3,  2,  2,  4,  5,  5]
pila_sin_duplicados = eliminar_duplicados_pila(pila_original)
print(pila_sin_duplicados)