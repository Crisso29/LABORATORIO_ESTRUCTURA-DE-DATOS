# 4 Escribir una función que encuentre la submatriz de mayor suma de una matriz:
import numpy as np
matriz=np.array([1,2,3,4,5])
def submatriz_maxima(matriz):
    fila, columna = matriz.shape
    max_val = 0
    max_submatriz = None

    for i in range(fila):
        for j in range(columna):
            if i + 1 < fila and j + 1 < columna:
                submatriz = matriz[i:i+2, j:j+2]
                suma = np.sum(submatriz)
                if suma > max_val:
                    max_val = suma
                    max_submatriz = submatriz
    return max_submatriz
