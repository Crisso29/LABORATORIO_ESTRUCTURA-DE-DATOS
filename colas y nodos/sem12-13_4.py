#Diseño de un sistema de gestión de tareas (Avanzado)
#4.    Implementa  un  sistema  de  gestión  de  tareas  que  permita  agregar  tareas,  marcar  tareas  como 
#completadas y mostrar la próxima tarea pendiente.
class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({'tarea': tarea, 'completada': False})
        print(f"Tarea '{tarea}' agregada.")

    def marcar_como_completada(self, tarea):
        for tarea_en_lista in self.tareas:
            if tarea_en_lista['tarea'] == tarea:
                tarea_en_lista['completada'] = True
                print(f"Tarea '{tarea}' marcada como completada.")
                return
        print(f"Tarea '{tarea}' no encontrada.")

    def mostrar_proxima_tarea_pendiente(self):
        for tarea in self.tareas:
            if not tarea['completada']:
                print(f"Próxima tarea pendiente: {tarea['tarea']}")
                return
        print("No hay tareas pendientes.")

# Ejemplo de uso
gestor = GestorTareas()

# Agregar tareas
gestor.agregar_tarea("Hacer la compra")
gestor.agregar_tarea("Llamar al médico")
gestor.agregar_tarea("Estudiar para el examen")

# Marcar una tarea como completada
gestor.marcar_como_completada("Hacer la compra")

# Mostrar la próxima tarea pendiente
gestor.mostrar_proxima_tarea_pendiente()
