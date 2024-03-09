#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de menor a mayor y que no están duplicados
def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados_set = set(sorted(conjunto_numeros))
    return numeros_ordenados_set

conjunto_ejemplo = {5, 2, 8, 3, 1, 7, 2, 8}
resultado = numeros_ordenados_sin_duplicados(conjunto_ejemplo)
print("Números ordenados de menor a mayor sin duplicados: ",resultado)
