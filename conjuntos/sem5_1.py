#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos
def primos():
    numbers=input("Ingresa los números que desees separados por comas: ").strip()
    list_p=numbers.split(",")
    list_p=list(map(int, list_p))
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    primos_filtrados = [p for p in list_p if es_primo(p)]
    return primos_filtrados

resultado =set(primos())
print("Números primos:", resultado)

