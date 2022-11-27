print ('Ejercicios de modulo 3.2.1.17')
'''Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:'''
for i in range(1, 11):
    # Línea de código.
        # Línea de código.
    i = i + 1
    while i % 2 != 0:
        print (i)
        break
print('fin de bucle..')
#------------------------------------------------------------
input("Presione una tecla para continuar a otro programa")
#------------------------------------------------------------
'''Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:'''
x = 1
while x < 11:
    print (x)
    if x < 11:
        x += 1
print ('fin')
#------------------------------------------------------------
input("Presione una tecla para continuar a otro programa")
#------------------------------------------------------------
'''Crea un programa con un bucle for y una sentencia break. El programa 
debe iterar sobre los caracteres en una dirección de correo electrónico, 
salir del bucle cuando llegue al símbolo @ e imprimir la parte antes 
de @ en una línea. Usa el esqueleto de abajo:'''

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    elif ch != '@':
        print (ch, end='')
#------------------------------------------------------------
'''
Crea un programa con un bucle for y una sentencia continue. El programa debe iterar sobre una cadena de dígitos, 
reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:
'''
for digit in "0165031806510":
    if digit == "0":
        print ("x", end='')
    elif digit !=0:
        print (digit, end='')
