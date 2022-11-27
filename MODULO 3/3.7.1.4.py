'''
    Imagina que desarrollas una pieza de software para una estación meteorológica automática. 
    El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. 
    Esto te da un total de 24 × 31 = 744 valores.
'''
#temps = [[0.0 for h in range(24)] for d in range(31)]
'''
    Ahora es el momento de determinar la temperatura promedio mensual del mediodía. Suma las 31 
    lecturas registradas al mediodía y divida la suma por 31. Puedes suponer que la temperatura 
    de medianoche se almacena primero.
'''
#temperatura = 0.0 (float)
#for dia in temperatura:
#    temperatura += dia[11]
#average = temperatura / 31
###################################################################################################

temps = [[0.0 for h in range(24)] for d in range(31)]
# La matriz se actualiza aquí.
highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("La temperatura más alta fue:", highest)
