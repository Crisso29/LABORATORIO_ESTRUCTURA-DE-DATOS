#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#comienzan con una letra determinada
def word():
    conj=set(input("Ingrese algunas palabras separadas por comas: ").strip().split(","))
    print(conj)
    
    letras = set(input("Ingrese las letras iniciales separadas por comas: ").strip().split(","))

    palabras_f = {palabra for palabra in conj if any(palabra.startswith(letra) for letra in letras)}
    return palabras_f

resultado = word()
print(resultado)