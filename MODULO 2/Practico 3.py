# Practico 3 : La hora inicial de un evento es a las 13:40 y dura 25 minutos
# escribir un programa que devuelva en pantalla la hora:minuto 
# de finalización
# se debe poder cargar otras hora:minuto de inicio y duración en minutos
# manteniendo el funcionamiento correcto del programa

hora_inicial = 13
minuto_inicial = 40
duracion = 25

min_fin = (minuto_inicial + duracion) % 60
hr_fin = hora_inicial + (minuto_inicial + duracion) // 60

print = (hr_fin, ":",min_fin)