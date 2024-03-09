#4 Asegurar que una lista no esté vacía
def lista(a):
    assert len(a)!=0, "la lista está vacía"
    return a, "=no está vacía"
a=[1,2]
listaa=lista(a)
print(listaa)