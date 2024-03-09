#Verificar si una palabra es palíndroma
#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.
from collections import deque

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = palabra.lower()
    
    # Crear una cola y agregar cada carácter de la palabra a la cola
    cola = deque()
    for char in palabra:
        if char.isalpha(): # Ignorar espacios y caracteres no alfabéticos
            cola.append(char)
    
    # Comparar los caracteres de la palabra en orden original y en orden inverso
    while len(cola) > 1:
        primer_caracter = cola.popleft() # Quitar el primer carácter de la cola
        ultimo_caracter = cola.pop() # Quitar el último carácter de la cola
        
        if primer_caracter != ultimo_caracter:
            return False # Si los caracteres no coinciden, no es un palíndromo
    
    return True # Si todos los caracteres coinciden, es un palíndromo

# Ejemplo de uso
palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")