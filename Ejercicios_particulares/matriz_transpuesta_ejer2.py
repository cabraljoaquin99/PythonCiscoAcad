#**Ejercicio 2: Matriz Transpuesta**
#Escribe un programa que tome una matriz y genere su matriz transpuesta. 
#La matriz transpuesta se obtiene intercambiando filas por columnas.

# Define la matriz original (3x3)
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializa la matriz transpuesta (3x3)
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Genera la matriz transpuesta
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz2[j][i] = matriz1[i][j]

# Imprime la matriz transpuesta
for fila in matriz2:
    print(fila)
