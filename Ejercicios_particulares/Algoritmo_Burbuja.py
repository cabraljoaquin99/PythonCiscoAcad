my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1): # Para que el conteo de la lista no quede fuera de rango se añade el "-1"
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ocurrira un intercambio en la prox linea -> sera True mientras el elemento actual sea mayor al adyacente,
                            # ocurriendo lo contrario, "swapped" sera false y saldra del bucle while, para imprimir la lista ordenada.
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
'''
Dentro del bucle for, se usa la condición 
if my_list[i] > my_list[i + 1]: para verificar si el elemento actual es mayor que el siguiente. 
Si es así, significa que están desordenados y se deben intercambiar.
'''
print(my_list)


#8 10 6 2 4
#8 6 10 2 4
#8 6 2 10 4
#8 6 2 4 10
#6 8 2 4 10
#6 2 8 4 10
#6 2 4 8 10
#2 6 4 8 10
#2 4 6 8 10