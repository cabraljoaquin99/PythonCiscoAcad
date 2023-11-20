'''
Se debe crear y cargar una lista donde almacenar 5 sueldos. 
Desplazar el valor mayor de la lista a la última posición.
La primera aproximación para llegar en el próximo problema al ordenamiento 
completo de una lista tiene por objetivo analizar los intercambios de elementos dentro de la lista 
y dejar el mayor en la última posición. El algoritmo consiste en comparar si la primera componente 
es mayor a la segunda, en caso que la condición sea verdadera, 
intercambiamos los contenidos de las 
componentes.
'''
sueldo = []

# Solicitar al usuario que ingrese 5 sueldos
for i in range(5):
    sueldo_actual = float(input("Ingrese el sueldo del operario: "))
    sueldo.append(sueldo_actual)
print("Los sueldos de los operarios son:", sueldo, "Antes de ordenar\n")

# Ordenar la lista de sueldos
for i in range(len(sueldo) - 1):
    flag = False
    for i in range(len(sueldo) - 1):
        if sueldo[i] > sueldo[i + 1]:
            sueldo[i], sueldo[i + 1] = sueldo[i + 1], sueldo[i]
            flag = True
    if not flag:
        break

print("Los sueldos ordenados son:\n", sueldo)

