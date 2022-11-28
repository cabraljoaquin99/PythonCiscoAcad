# 3.7.1.5 Listas en aplicaciones avanzadas â Arreglos
'''
    Python no limita la profundidad de la inclusión lista en lista. Aquí puedes ver un ejemplo de un arreglo tridimensional:
    Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. 
    Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y 
    procesar información sobre las habitaciones ocupadas/libres.
'''
#Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# El primer índice (0 a 2) selecciona uno de los edificios; el segundo (0 a 14) selecciona el piso, 
# el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas.
# r : habitaciones
# f : 15 pisos
# t : 3 edificios

#Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio(t), en el décimo piso(f), habitación 14(r):
rooms[1][9][13] = True
#y desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:
rooms[0][4][1] = False
#Verifica si hay disponibilidad en el piso 15 del tercer edificio:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
# La variable vacancy contiene 0 si todas las habitaciones están ocupadas, o en dado caso el número de habitaciones disponibles.
'''
    La comprensión de listas te permite crear nuevas listas a partir de las existentes de una manera concisa y elegante. 
    La sintaxis de una comprensión de lista es la siguiente:
    
    [expression for element in list if conditional]

    Este es un ejemplo de una comprensión de lista: el código siguiente crea una lista de cinco elementos con los primeros
    cinco números naturales elevados a la potencia de 3:
    cubed = [num ** 3 for num in range(5)]
    print(cubed)  # outputs: [0, 1, 8, 27, 64]
'''

