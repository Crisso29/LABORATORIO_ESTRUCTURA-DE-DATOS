#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en ambos conjuntos.
def intersección():
    conj_a=set(map(int, input("ingrese los numeros del conjunto A separados por comas: ").strip().split(",")))
    conj_b=set(map(int, input("Ingrese los elementos del conjunto B separados por comas: ").strip().split(",")))
    resultado=conj_a.intersection(conj_b)
    return resultado

inters=intersección()
print(inters)