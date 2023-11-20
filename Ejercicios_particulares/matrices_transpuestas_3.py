# Crear una lista de listas (una matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transponer la matriz
matriz_transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

# Ahora tienes la matriz transpuesta, que intercambia filas por columnas

# Sumar todas las filas y guardar los resultados en una lista
suma_filas = [sum(fila) for fila in matriz]

# Sumar todas las columnas y guardar los resultados en una lista
suma_columnas = [sum(columna) for columna in matriz_transpuesta]

# Imprimir los resultados
print("Suma de las filas:", suma_filas)
print("Suma de las columnas:", suma_columnas)
