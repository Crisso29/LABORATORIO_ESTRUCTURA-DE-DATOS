#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#son primos y están ordenados de menor a mayor.
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_ordenados(conjunto_numeros):
    primos_set = {numero for numero in conjunto_numeros if es_primo(numero)}
    primos_ordenados_set = set(sorted(primos_set))
    return primos_ordenados_set

conjunto_ejemplo = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
resultado = primos_ordenados(conjunto_ejemplo)
print("Números primos ordenados de menor a mayor: ", resultado)
