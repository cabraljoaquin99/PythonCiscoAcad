'''
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos.
'''
promedio = float (.0)
sueldos = []
for x in range (5):
    sueldo = float (input (f"Ingrese el sueldo de hasta 5 operarios {x+1}: "))
    sueldos.append (sueldo)
    promedio = sum (sueldos) / len(sueldos)

print ("El sueldo promedio entre 5 empleados es: \n", promedio)
