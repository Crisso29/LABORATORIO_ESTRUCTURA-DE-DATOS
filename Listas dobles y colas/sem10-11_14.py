#Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres
class Pila:
    def __init__(self):
        self.elementos = []
    def push(self, elemento):
        self.elementos.append(elemento)
    def pop(self):
        if not self.vacia():
            return self.elementos.pop()
    def vacia(self):
        return len(self.elementos) ==  0

class SistemaDeshacer:
    def __init__(self):
        self.acciones = Pila()
        self.deshaceres = Pila()

    def agregar(self, elemento):
        self.acciones.push(('agregar', elemento))

    def eliminar(self, elemento):
        self.acciones.push(('eliminar', elemento))

    def deshacer(self):
        if not self.acciones.vacia():
            accion, elemento = self.acciones.pop()
            self.deshaceres.push((accion, elemento))
            if accion == 'agregar':
                print(f"Deshaciendo: eliminando {elemento}")
            else:
                print(f"Deshaciendo: agregando {elemento}")

    def rehacer(self):
        if not self.deshaceres.vacia():
            accion, elemento = self.deshaceres.pop()
            self.acciones.push((accion, elemento))
            if accion == 'eliminar':
                print(f"Rehaciendo: agregando {elemento}")
            else:
                print(f"Rehaciendo: eliminando {elemento}")

# Ejemplo de uso
sistema = SistemaDeshacer()

# Agregando elementos
sistema.agregar('elemento1')
sistema.agregar('elemento2')

# Deshaciendo una acción
sistema.deshacer()

# Rehaciendo una acción
sistema.rehacer()
