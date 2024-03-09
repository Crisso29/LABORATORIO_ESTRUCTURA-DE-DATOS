#. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de mayor a menor.
def numeros_ordenados_descendente(conjunto_numeros):
    conjunto_ordenado_descendente = set(sorted(conjunto_numeros, reverse=True))
    return conjunto_ordenado_descendente

conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
resultado = numeros_ordenados_descendente(conjunto_ejemplo)
print("Números ordenados de mayor a menor: ",resultado)