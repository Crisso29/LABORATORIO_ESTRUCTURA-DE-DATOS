
#Diseño de un sistema de gestión de pedidos
#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
#fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
#actual de la cola.
from collections import deque

class Pedido:
    def __init__(self, id_pedido, descripcion):
        self.id_pedido = id_pedido
        self.descripcion = descripcion

    def __str__(self):
        return f"Pedido {self.id_pedido}: {self.descripcion}"

class GestorPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido {pedido.id_pedido} agregado a la cola.")

    def procesar_pedido(self):
        if not self.cola_pedidos:
            print("No hay pedidos en la cola.")
            return
        pedido_procesado = self.cola_pedidos.popleft()
        print(f"Procesando: {pedido_procesado}")
        # Aquí puedes agregar el código para procesar el pedido

    def mostrar_estado(self):
        print("Estado actual de la cola de pedidos:")
        for pedido in self.cola_pedidos:
            print(pedido)

# Ejemplo de uso
gestor = GestorPedidos()

# Agregar pedidos a la cola
gestor.agregar_pedido(Pedido(1, "Pizza grande"))
gestor.agregar_pedido(Pedido(2, "Hamburguesa"))

# Procesar el primer pedido en la cola
gestor.procesar_pedido()

# Mostrar el estado actual de la cola
gestor.mostrar_estado()