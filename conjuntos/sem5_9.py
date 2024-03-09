#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#tienen una longitud determinada.
def palabras_con_longitud(conjunto_palabras, longitud_deseada):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud_deseada}
    return palabras_seleccionadas

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
longitud_deseada = 4

resultado_palabras = palabras_con_longitud(conjunto_palabras, longitud_deseada)

print(f"Palabras con longitud {longitud_deseada}:", resultado_palabras)