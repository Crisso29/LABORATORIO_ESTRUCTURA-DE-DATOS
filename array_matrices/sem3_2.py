#Crea una matriz de números complejos
import numpy as np
def matriz_i():
    f=int(input("filas: "))
    c=int(input("columnas: "))
    matriz_imaginario=np.random.randint(0,10, size=(f,c), dtype=int)+ 1j*np.random.rand(f,c)
    return matriz_imaginario
print(matriz_i())