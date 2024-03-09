import numpy as np 
arreglos=np.array([1,2,4,3,2,1,0])
arreglos.sort()
print(arreglos)

for i in range(len(arreglos)):
    print(i)

name=int(input("Ingrese: "))
c=0
for j in range ( len(arreglos)):
    if arreglos[j]==name: 
        c+=1
print(c)

def create_array(TipoDeDato):
    cantidad=int(input("Cuantos lementos quisieras crear?: "))
    array=np.empty(cantidad, dtype=TipoDeDato)
    for i in range(cantidad):
        array[i]=TipoDeDato(input(f"Ingrese los numeros {i}: "))
    print(array)
create_array(int)



def crearMatriz():
    f = int(input("Ingrese la cantidad de filas: "))
    c = int(input("Ingrese la cantidad de columnas: "))
    matriz = np.empty([f, c], dtype=int)

    for x in range(f):
        for y in range(c):
            elemen = int(input("Coordenadas [{},{}]: ".format(x+1, y+1)))
            matriz[x, y] = elemen

    return matriz

matriz_creada = crearMatriz()
print("La matriz creada es:\n", matriz_creada)