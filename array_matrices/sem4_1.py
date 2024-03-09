
#1 Cree una matriz de números aleatorios de tamaño 100x100:
import numpy as np
def cien_cien():
    f=int(input("filas: "))
    c=int(input("columnas: "))
    matriz=np.random.randint(0,100, size=(f,c), dtype=int)
    return matriz
print(cien_cien())
#---------------------------------------------------------------------------------------------------------
