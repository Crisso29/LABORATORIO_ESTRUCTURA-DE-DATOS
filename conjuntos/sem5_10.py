#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#contienen una letra determinada.
def palabras_con_letra(conjunto_palabras, letra_deseada):
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if letra_deseada in palabra}
    return palabras_seleccionadas

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}
letra_deseada = "o"

resultado_palabras = palabras_con_letra(conjunto_palabras, letra_deseada)

print(f"Palabras que contienen la letra '{letra_deseada}':", resultado_palabras)