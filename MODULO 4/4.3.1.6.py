'''
Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, 
es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, 
es un año común.
De lo contrario, es un año bisiesto.


#Este código

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
'''
def es_bisiesto (yr):
# Falta código ...
#
# def 'algo' esta definiendo una función
test_years = [1900, 2000, 2016, 1987]
#test_months = [2, 2, 1, 11]
test_results = [False, True, True, False]

for i in range (len(test_years)):
    yr = test_years[i]
    print(yr, "->", end="")
    result = es_bisiesto(yr)
    if result == test_results[i]:
        print ("OK")
        print True
    else:
        print ("Fallido")
        print False
