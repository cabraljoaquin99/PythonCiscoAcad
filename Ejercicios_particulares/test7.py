'''
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
'''
lista = []

mayores_a = 0
menores_a = 0

for i in range (5):
    alturas = float (input (f"Ingrese hasta 5 alturas, la número..{i+1}: \n"))
    lista.append (alturas)
    promedio = sum (lista) / len (lista)
   
    flag = True
    while flag == True:
        flag = False
        if (alturas > promedio): #si alturas > a promedio, mostrar cuantas son más altas, y por otro lado aquellas más bajas
            mayores_a += 1
        else:
            menores_a += 1
print ("El promedio de las alturas es: \n", promedio)
print ("Las alturas menores a el promedio son:", menores_a)
print ("Las alturas mayores a el promedio son:", mayores_a)
