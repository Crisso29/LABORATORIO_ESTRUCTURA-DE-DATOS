#Crea una matriz de matrices.
import numpy as np
def matriz_matriz():
    f=int(input("filas: "))
    c=int(input("columnas: "))
    matriz=np.empty([f,c], dtype=object)
    for x in range(f):
        for y in range(c):
            f1=int(input("filas de submatrices: "))
            c1=int(input("columnas de submatrices: "))
            matriz[x , y]=np.random.rand(f1,c1)
    return matriz
resultado=matriz_matriz()
print(resultado)
