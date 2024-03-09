#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de menor a mayor.
def numeros_ordenados(conjunto_numeros):
    conjunto_ordenado = set(sorted(conjunto_numeros))
    return conjunto_ordenado

conjunto_ejemplo = {5, 2, 8, 3, 1, 7}
resultado = numeros_ordenados(conjunto_ejemplo)
print("Números ordenados de menor a mayor: ",resultado)