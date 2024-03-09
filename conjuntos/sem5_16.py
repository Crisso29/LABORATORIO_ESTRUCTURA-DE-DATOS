#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#palíndromos y están ordenadas de menor a mayor.
def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_ordenados(conjunto_palabras):
    palindromos_set = {palabra for palabra in conjunto_palabras if es_palindromo(palabra)}
    palindromos_ordenados_set = set(sorted(palindromos_set))
    return palindromos_ordenados_set

conjunto_ejemplo = {"radar", "python", "level", "Scratch", "Java"}
resultado = palindromos_ordenados(conjunto_ejemplo)
print("Palíndromos ordenados de menor a mayor: ", resultado)