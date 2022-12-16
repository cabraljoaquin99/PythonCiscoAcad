'''
    Escribir un par de funciones que 
    conviertan l/100km a mpg (milas por galón), 
    y viceversa.
'''

# 1 milla (mile) = 1609.344 metros(metres)
# 1 galón (gallon) = 3.785411784 litros(litres)

def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

'''
liters_100km_to_miles_gallon y 
miles_gallon_to_liters_100km. 

La primera función convierte de l/100km a mpg y 
la segunda función convierte de mpg a l/100km.

En la función liters_100km_to_miles_gallon, primero se 
convierten los litros a galones utilizando la fórmula:

gallons = litres / 3.785411784

Luego, se convierten los 100 km a millas utilizando
la fórmula:

miles = 100 * 1000 / 1609.344

Finalmente, se divide la cantidad de millas por la 
cantidad de galones para obtener el consumo en mpg.
En la función miles_gallon_to_liters_100km, primero 
se convierten las millas a km utilizando la fórmula:

km100 = miles * 1609.344 / 1000 / 100

Luego, se divide la cantidad de litros por la cantidad
de km para obtener el consumo en l/100km.

El parámetro litres sí tiene un valor asignado, ya que
se le pasa como argumento cuando se llama a la 
función. Por ejemplo, cuando se llama a la función 
liters_100km_to_miles_gallon(3.9), el valor de litres 
es 3.9 dentro de la función.

La forma en que se pasan argumentos a una función se 
llama "llamada por valor". Esto significa que cuando 
se llama a la función y se le pasa un argumento, el 
valor del argumento se copia en la variable local de 
la función. En este caso, el valor de litres se copia 
en la variable local litres dentro de la función.
'''
 