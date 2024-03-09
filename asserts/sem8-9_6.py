# 6 Asegurar que un ciclo while ejecute al menos una vez
def asegurar():
    contador=0
    while contador<10:
        contador+=1
    assert contador==10, "EL ciclo while no se ejecutó al menos una vez"
print(asegurar())
