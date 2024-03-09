#Búsqueda de rutas en un laberinto
#3.    Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
#para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.
from collections import deque

def encontrar_camino(laberinto):
    # Encontrar la posición inicial y final
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 'S':
                inicio = (i, j)
            if laberinto[i][j] == 'D':
                destino = (i, j)

    # Inicializar la cola y el diccionario de visitados
    cola = deque([inicio])
    visitados = {inicio: None}

    while cola:
        x, y = cola.popleft()
        if (x, y) == destino:
            # Construir el camino más corto
            camino = []
            while (x, y) != inicio:
                camino.append((x, y))
                x, y = visitados[(x, y)]
            camino.append(inicio)
            camino.reverse()
            return camino

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(laberinto)) and (0 <= ny < len(laberinto[0])) and (laberinto[nx][ny] != '#') and (nx, ny) not in visitados:
                cola.append((nx, ny))
                visitados[(nx, ny)] = (x, y)

    return None # No se encontró un camino

# Ejemplo de laberinto
laberinto = [
    ['S', '.', '.', '.', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', 'D'],
]

camino = encontrar_camino(laberinto)
if camino:
    print("Camino encontrado:")
    for x, y in camino:
        print(f"({x}, {y})", end=" -> ")
    print("Destino")
else:
    print("No se encontró un camino.")
