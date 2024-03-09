#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#tienen una longitud determinada y están ordenadas de menor a mayor
def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_f = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    palabras_ordenadas_set = set(sorted(palabras_f))
    return palabras_ordenadas_set

conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
longitud_deseada = 5
resultado = palabras_longitud_ordenadas(conjunto_ejemplo, longitud_deseada)
print("Palabras de longitud ", longitud_deseada, "ordenadas de menor a mayor: ", resultado)


