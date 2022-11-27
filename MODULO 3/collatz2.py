n1 = int (input ("Ingresa un número natural positivo: "))
contador = 0
while n1 > 1:
    if n1 % 2 == 0:
        n1 = n1 // 2
        print ("Instancia par: ", n1)
    else:
        n1 = (n1*3) + 1
        print ("Instancia impar: ", n1)
        contador += 1
print ("Cantidad de pasos: ", contador)