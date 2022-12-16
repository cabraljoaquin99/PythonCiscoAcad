'''
Para determinar si un año es bisiesto, podemos utilizar la siguiente fórmula:

if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)

Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes 
y un día del mes) y devuelve el día correspondiente del año, o devuelve None 
si cualquiera de los argumentos no es válido.

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # Usamos un diccionario para almacenar el número de días
    # en cada mes.
    days_in_month = {
        1: 31,  # Enero tiene 31 días
        2: 28,  # Febrero tiene 28 días (por defecto)
        3: 31,  # Marzo tiene 31 días
        4: 30,  # Abril tiene 30 días
        5: 31,  # Mayo tiene 31 días
        6: 30,  # Junio tiene 30 días
        7: 31,  # Julio tiene 31 días
        8: 31,  # Agosto tiene 31 días
        9: 30,  # Septiembre tiene 30 días
        10: 31, # Octubre tiene 31 días
        11: 30, # Noviembre tiene 30 días
        12: 31  # Diciembre tiene 31 días
    }

    # Si el año es bisiesto y el mes es febrero,
    # aumentamos en 1 el número de días.
    if is_year_leap(year) and month == 2:
        days_in_month[2] += 1

    # Devolvemos el número de días para el mes dado.
    return days_in_month[month]

# Pruebas para verificar el correcto funcionamiento de la función
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
'''