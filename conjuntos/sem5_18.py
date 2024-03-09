#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#contienen una letra determinada y están ordenadas de mayor a menor.

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_ordenadas_set = set(sorted(palabras_filtradas, reverse=True))
    return palabras_ordenadas_set

conjunto_ejemplo = {"python", "java", "shard", "javascript", "level"}
letra_deseada = "a"
resultado = palabras_con_letra_ordenadas(conjunto_ejemplo, letra_deseada)
print("Palabras con la letra ", letra_deseada, " ordenadas de mayor a menor: ",resultado)