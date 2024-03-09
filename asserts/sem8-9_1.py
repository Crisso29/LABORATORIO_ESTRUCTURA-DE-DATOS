#1 Validar la edad de un usuario
def edad(num):
    assert 12<=num<=18, "no se acepta este edad"
    return num
num=int(input("INGRESA TU EDAD \nsolo puedes ingresar una edad en el rango de 12 a 18: "))
TuEdad=edad(num)
print(TuEdad)

#7 Asegurar que una función retorne un valor específico
def función():
    return 4
assert función()!=4, "La función no retornó el valor esperado"
print(función())
