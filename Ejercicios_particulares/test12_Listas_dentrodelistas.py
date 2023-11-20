# Definir dos matrices como listas anidadas
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Inicializar una matriz vacía para almacenar la suma
suma_matriz = []

# Asumimos que las dos matrices tienen las mismas dimensiones
filas = len(matriz1)
columnas = len(matriz1[0])

# Recorremos las filas y columnas para sumar los elementos
for i in range(filas):
    fila = []
    for j in range(columnas):
        suma = matriz1[i][j] + matriz2[i][j]
        fila.append(suma)
    suma_matriz.append(fila)

# Imprimir la suma de las matrices
for fila in suma_matriz:
    print(fila)
