#Crea una matriz de números reales.
import numpy as np
def matriz_real():
    filas=int(input("cuantas filas quieres?: "))
    columnas=int(input("cuántas columnas deseas?: "))
    element=np.random.rand(filas,columnas)
    return element

resultado= matriz_real()
print("tu matriz es:\n", resultado)