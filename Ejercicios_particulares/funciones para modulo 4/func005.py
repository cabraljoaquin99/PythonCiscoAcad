#Confeccionar una función que le enviemos como parámetros 
#dos enteros y nos retorne el mayor.

def enteros(uno,dos):
    primero = uno
    segundo =  dos

    if primero > segundo:
        print (primero)
        return primero
    else:
        print (segundo)
        return segundo

uno = int (input ("Ingrese hasta dos valores enteros: "))
dos = int (input ("Otro "))

salida = enteros(uno, dos)