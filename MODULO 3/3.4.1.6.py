hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
print(hat_list)
ingreso = int (input ('Ingrese un numero: \n'))
hat_list[2]= ingreso
print(hat_list)
input('Ingrese una tecla para continuar el programa')
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list [4]
print(hat_list)
input('Ingrese una tecla para continuar el programa')
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print ("La longitud de la lista es: ", end='')
print (len(hat_list))