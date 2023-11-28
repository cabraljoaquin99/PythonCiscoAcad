'''
En un curso de 4 alumnos se registraron las notas de sus exámenes y se 
deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. 
En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" 
si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”. '''

# Inicializar las listas para nombres y notas
nombres = []
notas = []

# Solicitar y almacenar los nombres y notas de los alumnos
for i in range(4):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))  
    # Convertir la entrada a tipo float
    
    nombres.append(nombre)
    notas.append(nota)

# Mostrar el listado de nombres, notas y condición del alumno
print("Listado de alumnos:")
for i in range(len(nombres)):
    nombre_actual = nombres[i]
    nota_actual = notas[i]
    
    # Determinar la condición del alumno según la nota
    if nota_actual >= 8:
        condicion = 'Muy Bueno'
    elif 4 <= nota_actual <= 7:
        condicion = 'Bueno'
    else:
        condicion = 'Insuficiente'
    
    # Mostrar nombre, nota y condición del alumno
    print(f"Nombre: {nombre_actual}, Nota: {nota_actual}, Condición: {condicion}")

# Contar cuántos alumnos tienen la leyenda “Muy Bueno”
contador_muy_bueno = sum(1 for nota in notas if nota >= 8)
print(f"Cantidad de alumnos con la leyenda 'Muy Bueno': {contador_muy_bueno}")
