#3 Escribir una función que encuentre el elemento máximo de una matriz:
import numpy as np
matriz_aleatoria=np.array([1,2,3,4,5])
def maximo(matriz):
    return np.max(matriz)

print("Elemento máximo: ", maximo(matriz_aleatoria))