#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#palíndromos.
def palindromo(palabra):
    return palabra == palabra[::-1]

def palindromos_en_conjunto(conjunto_palabras):
    
    palindromos = {palabra for palabra in conjunto_palabras if palindromo(palabra)}
    return palindromos

conjunto_palabras = {"oso", "reconocer", "hola", "radar", "python", "civic"}

resultado_palindromos = palindromos_en_conjunto(conjunto_palabras)

print("Conjunto de palíndromos:", resultado_palindromos)