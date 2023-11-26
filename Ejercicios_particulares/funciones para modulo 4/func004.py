#El Programa puede ser hecho con funcion/es , no es asi originalmente
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=17&codigo=17&inicio=15

#Hacer con funcion:
#Crear y cargar dos listas con los nombres de 5 productos en una 
#y sus respectivos precios en otra. Definir dos listas paralelas. 
#Mostrar cuantos productos tienen un precio 
#mayor al primer producto ingresado.
def comparativa (precios):
    primer_precio = precios[0]
    mayores = []
    for precio in precios[1:]:
        if precio > primer_precio:
            mayores.append(precio)
    return mayores

productos = []
precios = []

for i in range (5):
    in_productos = (input (f"Ingrese hasta {range} productos: "))
    print (f"Ingreso {i} nombres de producto/s")
    productos.append(in_productos)

for y in range (5):
    print ("\n")
    print ("***************************************************")
    in_precios = int (input (f"Ingrese hasta {range} precios: "))
    precios.append(in_precios)
    print (f"Ingreso {y} precios de producto/s")
    
resultados = comparativa (precios)

if resultados:
    print ("Los precios mayores al primero son :", resultados)
else:
    print("No hay precios mayores al primero en la lista.")
