#5 Validar la igualdad de dos objetos
def objeto(a,b):
    assert a==b, "Los objetos no son iguales"
    return a,b,  "son iguales"
a=3
b=4
objet=objeto(a,b)
print(objet)