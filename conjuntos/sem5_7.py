#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#anagramas.
def anagramas():
    conj1=set(input("Ingrese cualquier palabra: "))
    conj2=set(input("Ingrese otra palabra para comprobar: "))
    if conj1==conj2:
        print("Es anagrama")
    else:
        
        print("\nSabes que no van a ser anagramas🙄")
anagramas()