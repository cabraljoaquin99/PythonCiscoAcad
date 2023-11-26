'''
Cargar una lista con 5 elementos enteros. 

Imprimir el mayor y un mensaje si se repite dentro de la lista 

(es decir si dicho valor se encuentra en 2 o más 
posiciones en la lista)
'''

lista = []

# Cargar la lista con 5 elementos enteros
for i in range(5):
    ingreso = int(input("Ingrese un número entero: "))
    lista.append(ingreso)

# Encontrar el número mayor en la lista
mayor = max(lista)
print("El número mayor en la lista es:", mayor)

# Verificar si el número mayor se repite en la lista
repeticiones = lista.count(mayor)
if repeticiones >= 2:
    print(f"El número {mayor} se repite {repeticiones} veces en la lista.")
else:
    print(f"El número {mayor} no se repite en la lista.")

print("Fin del programa")
