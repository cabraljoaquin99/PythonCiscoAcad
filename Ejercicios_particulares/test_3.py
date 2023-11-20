'''
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
'''

alturas = []

for i in range (5):
    cantidad = float (input ("Ingrese hasta 5 valores de alturas en decimal punteado: "))
    alturas.append(cantidad)

promedio = sum(alturas) / len(alturas)
print ("El promedio de estos ingresos son: ", promedio)

# Contar cuántas personas son más altas y cuántas son más bajas que el promedio
mas_altas = sum(altura > promedio for altura in alturas)
mas_bajas = sum(altura < promedio for altura in alturas)

# Imprimir resultados
print(f"Promedio de alturas: {promedio:.2f} metros")
print(f"Personas más altas que el promedio: {mas_altas}")
print(f"Personas más bajas que el promedio: {mas_bajas}")
#En este código, primero se solicita al usuario ingresar las alturas de las personas 
#y se almacenan en una lista. Luego, se calcula el promedio de las alturas y se cuentan cuántas personas son más altas y cuántas son más bajas que el promedio. Finalmente, se imprimen los resultados.
