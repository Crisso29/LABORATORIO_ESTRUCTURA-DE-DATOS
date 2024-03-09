#Accede al elemento central de una matriz
filas = 5
columnas = 5
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        #* Puedes ingresar cualquier valor deseado, aquí se usa un valor único para simplificar el ejemplo
        fila.append(i * columnas + j)
    matriz.append(fila)

# Mostrar la matriz
print("Matriz:")
for fila in matriz:
    print(fila)

#* Calcular las coordenadas del elemento central
fila_central = filas // 2
columna_central = columnas // 2

#*  Acceder al elemento central
elemento_central = matriz[fila_central][columna_central]
print("Elemento central:", elemento_central)
