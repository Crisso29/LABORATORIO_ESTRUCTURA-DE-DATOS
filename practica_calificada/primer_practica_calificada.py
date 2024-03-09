#Ingresar un conjunto de números y devolver en una lista todos los no primos
def no_primos():
    numbers=set(map(int, input("Ingresa los números que desees separados por comas: ").strip().split(",")))
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    no_primos_filtrados = [p for p in numbers if not es_primo(p)]
    return no_primos_filtrados

resultado =set(no_primos())
print("Números primos:", resultado)
