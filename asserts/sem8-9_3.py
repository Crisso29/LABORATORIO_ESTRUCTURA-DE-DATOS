#3 Validar el rango de una calificación
def rango_calificación(calificación):
    assert 10.5<=calificación<=20, "Desaprobaste"
    return calificación, "CONGRATULATION"
calificación=float(input("Ingresa la nota: "))
b=rango_calificación(calificación)
print(b)