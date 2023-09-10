'''
Evaluar o encontrar el tiempo final 
de un periodo de tiempo dado, expresándolo en horas y minutos. 
Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado 
en la consola.

12
17
59
Salida esperada: 13:16

'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

calc_mins = (dura + mins / 60) 
#modulo_mins = (dura + mins % 60)
calc_hour = hour + calc_mins
print ("La duración del evento en minutos es ", calc_hour, calc_mins)
