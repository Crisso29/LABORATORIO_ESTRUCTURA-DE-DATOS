#9 Asegurar que un módulo se ha importado correctamente
import sys
def importar_modulo(nombre_modulo):
    try:
        __import__(nombre_modulo)
    except ModuleNotFoundError as e:
        print(f"Error al importar el módulo {nombre_modulo}: {e}")
        return False
    
    assert nombre_modulo in sys.modules, f"El módulo {nombre_modulo} no se ha importado correctamente."
    print(f"El módulo {nombre_modulo} se ha importado correctamente.")
    return True