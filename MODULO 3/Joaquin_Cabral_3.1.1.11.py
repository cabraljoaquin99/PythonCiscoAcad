# https://edube.org/learn/python-essentials-1-esp/laboratorio-fundamentos-de-la-sentencia-if-else

Ingreso_ciudadano = float(input("Ingrese un valor, en formato decimal: "))
if Ingreso_ciudadano > 0 and Ingreso_ciudadano <= 85528:
    Impuesto_a = (Ingreso_ciudadano * 0.18) - 556.02
    Impuesto_a = round (Impuesto_a, 0)
    print ('El impuesto a pagar ', Impuesto_a)
else:
    if Ingreso_ciudadano > 85528:
        Impuesto_a = 14839.02 + (Ingreso_ciudadano - 85528) * 0.32
        Impuesto_a = round (Impuesto_a, 0)
        print ('El impuesto a pagar ', Impuesto_a)
    else:
        print ("No hay impuesto a pagar")