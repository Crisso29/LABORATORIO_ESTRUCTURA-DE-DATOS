#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#son divisibles por un número determinado
def num():
    nume=set(map(int, input("ingrese los numeros deseados separados por comas: ").strip().split(",")))
    print(num)
    div=int(input("ingrese un numero con que quieras dividir: "))
    result={numero for numero in nume if numero%div==0}
    return result

re=num()
print(re)