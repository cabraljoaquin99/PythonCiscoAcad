'''
Definir una lista por asignación que almacene en el
primer componente el nombre de un alumno y en las dos siguientes sus notas. 
Imprimir luego el nombre y el promedio de las dos notas.

alumno=["juan"]
notas=[8,10]
print("Nombre:\n", alumno[0])
print("Notas:\n", (notas[0]+notas[1]) / 2)
'''
# Definir por asignación una lista con 8 elementos enteros. Contar cuantos de 
# dichos valores almacenan un valor superior a 100.
elementos = [12,24,3,42,555,6,70,9]
cantidad = 0
x = 0
while x < len (elementos): # len ???
    if elementos[x] > 100:   #ver en el debugger
        cantidad += 1
    x += 1
print ("La lista contiene los valores: \n")
print(elementos)
print("Cantidad de valores mayores a 100 que hay en la lista: ")
print(cantidad)
