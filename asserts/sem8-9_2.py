#2 Verificar el tipo de dato de un variable
def tipoVariable(var):
    assert isinstance(var, float), "EL VALOR QUE INGRESASTE NO ES NÚMERO!!!"
    return var, "tu si haces caso"
print(tipoVariable(4.))
