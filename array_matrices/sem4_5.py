# 5 Escribir una función que encuentre la matriz de covarianza de dos matrices:
import numpy as np
matriz1=np.array([1,2,3,4,5])
matriz2=np.array([2,3])
def matriz_covarianza(matriz1, matriz2):
    return np.cov(matriz1, matriz2)

# Crear dos matrices para el ejemplo
matriz1 = np.random.rand(100, 100)
matriz2 = np.random.rand(100, 100)

print("Matriz de covarianza: \n", matriz_covarianza(matriz1, matriz2))