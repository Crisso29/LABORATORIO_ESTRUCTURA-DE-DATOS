#8 Validar el estado de una variable después de una operación
def variable():
    a=2
    a-=1
    assert a==1, "EL estado de la variable no es el esperado de la operació"
print(variable())