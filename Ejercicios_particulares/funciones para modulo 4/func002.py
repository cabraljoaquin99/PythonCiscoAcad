#Desarrollar un programa con dos funciones.
#La primer solicite el ingreso de un entero y muestre el
#cuadrado de dicho valor. La segunda que solicite la carga de dos
#valores y muestre el producto de los mismos.
#Llamar desde el bloque del programa principal a ambas funciones.

def ingreso_entero():
    cuadrado1 = int (input("Ingrese un valor entero "))
    total_c = (cuadrado1**2)
    print ("El cuadrado es :", total_c)
    return total_c

def dos_val():
    valor1 = int (input("Ingrese dos valores "))
    valor2 = int (input("el ultimo "))
    producto = valor1* valor2
    print("El producto de los valores es: ", producto)
    return producto
   
resultado_cuadrado = ingreso_entero()
resultado_producto = dos_val()
