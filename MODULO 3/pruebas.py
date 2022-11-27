'''
for x in range (1, 10, 2):
    bucle = int (input ("Ingrese num: "))
    bucle = bucle *2
    print (bucle)
    if bucle <= 90:
        break
    elif bucle > 90:
        continue 
    print('El número total es: ')
    print (bucle)
'''

# Colecciones de datos 3.4.1.2 'https://edube.org/learn/python-essentials-1-esp/listas-colecciones-de-datos-indexaci-oacute-n-2'
'''
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido de la lista actual.
'''
#Y ahora queremos copiar el valor del quinto elemento al segundo elemento. ¿Puedes adivinar cómo hacerlo?
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[4] = numbers [1]
print("Nuevo contenido de la lista: ", numbers)  # Contenido de la lista actual.

#LISTA, INVERTIR EL ORDEN USANDO UN BUCLE FOR.. EJEMPLO

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
