#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no
#están duplicados.
def numeros_no_duplicados(conjunto_numeros):
    numeros_set = set()
    duplicados_set = set()

    for numero in conjunto_numeros:
        if numero in numeros_set:
            duplicados_set.add(numero)
        else:
            numeros_set.add(numero)

    numeros_no_duplicados_set = numeros_set - duplicados_set
    return numeros_no_duplicados_set

conjunto_ejemplo = {1, 2, 3, 2, 4, 5, 3, 6}
resultado = numeros_no_duplicados(conjunto_ejemplo)
print("Números no duplicados en el conjunto: ", resultado)
