#https://edube.org/learn/python-essentials-1-esp/laboratorio-fundamentos-de-la-sentencia-if-elif-else
'''
Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común.
De lo contrario, es un año bisiesto.
'''

year = int(input("Introduce un año: "))
a = int (0)


if year % 4 == 0 and year >= 1582:
    print ("Año Bisiesto")
else:
    if year %100 == 0 and year >= 1582:
        print ("Año Bisiesto")
    else:
        if year %400 == 0 and year >= 1582:
            print ("Año Bisiesto")
        elif year %400 != 0 and year >= 1582:
            print ("Año Común")
        elif year < 1582:
            print ("No esta dentro del período del calendario Gregoriano")
