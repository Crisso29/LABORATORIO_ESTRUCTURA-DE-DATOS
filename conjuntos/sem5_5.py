#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en el primer conjunto pero no en el segundo.
def diferencia():
    c1=set(map(int, input("Ingrese el primer conjunto separado por comas: ").strip().split(",")))
    c2=set(map(int, input("Ingrese el segundo conjunto separado por comas también: ").strip().split(",")))
    c3=c2.difference(c1)
    return c3
a=diferencia()
print(a)