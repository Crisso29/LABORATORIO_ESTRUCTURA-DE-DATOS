#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.
def es_palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_longitud_ordenados(conjunto_palabras, longitud):
    palindromos_set = {palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud}
    palindromos_ordenados_set = set(sorted(palindromos_set))
    return palindromos_ordenados_set

conjunto_ejemplo = {"level", "radar", "python", "deified", "hello"}
longitud_deseada = 5
resultado = palindromos_longitud_ordenados(conjunto_ejemplo, longitud_deseada)
print("Palíndromos de longitud ",longitud_deseada, "ordenados de menor a mayor: ",resultado)