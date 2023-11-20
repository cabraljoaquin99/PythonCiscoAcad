'''
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. 
Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.
'''

lista = []

ingresos = int (input ("Ingrese cuantos valores ud quiera, pero sepa que al ingresar cero, cierra el programa "))
ingresos2 = 0
print (ingresos2)
for x in range (ingresos):
    valores = int (input ("Ahora ingrese que valores desea: \n"))
    if valores == 0:
        ingresos2 = len(lista)
        ingresos -= ingresos2
        #print ("El resto,\n", ingresos)
        break
    else:
        lista.append(valores)
        for s in range (ingresos):
            if x == s:
                print ("La cantidad de valores que quiso ingresar: \n", ingresos)
print ("****************************************************************\n")
print ("\n")
print ("Si ud ingreso 0 durante la carga, le faltaron: \n", ingresos)
print ("Los valores ingresados por teclado son: \n", lista)
print ("El tamaño de la lista es: ", len(lista))
