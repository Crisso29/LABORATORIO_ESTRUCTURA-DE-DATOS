#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están duplicados.
def numeros_duplicados(conjunto_numeros):
    numeros_set = set()
    duplicados_set = set()

    for numero in conjunto_numeros:
        if numero in numeros_set:
            duplicados_set.add(numero)
        else:
            numeros_set.add(numero)

    return duplicados_set

conjunto_ejemplo = {1, 2, 3, 2, 4, 5, 3, 6}
resultado = numeros_duplicados(conjunto_ejemplo)
print("Números duplicados en el conjunto: ", resultado)