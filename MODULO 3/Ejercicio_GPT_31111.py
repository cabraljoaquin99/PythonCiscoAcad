'''En un país llamado "Econolandia", la gente está obligada a pagar impuestos sobre sus ingresos anuales. 
El impuesto se calcula de la siguiente manera:

Si el ingreso anual es de hasta 60,000 dólares, el impuesto es del 10% de los ingresos.
Si el ingreso anual es mayor de 60,000 dólares pero no supera los 100,000 dólares, el impuesto es del 20% de los ingresos.
Si el ingreso anual es de 100,000 dólares o más, el impuesto es del 30% de los ingresos.
Si los ingresos anuales son inferiores a 10,000 dólares, la persona está exenta de impuestos.

Tu tarea es escribir un programa que calcule el impuesto a pagar por una persona y muestre el resultado.

El programa debe aceptar un valor de punto flotante que representa el ingreso anual de la persona y luego 
imprimir el impuesto calculado, redondeado a dólares enteros utilizando la función round().

Asegúrate de que tu programa tenga en cuenta las reglas de exención fiscal para ingresos bajos.
'''

impuesto = 0.0
ingreso = float(input("Inserte un valor de ingreso anual: "))

if ingreso >= 100000:
    # Calcular el 30% sobre el valor de los ingresos
    impuesto = float(ingreso * 30 / 100) 
    impuesto = round(impuesto, 2)  # Redondear a 2 decimales
    print(f"El valor del impuesto para su ingreso será de: ${impuesto}")
elif ingreso >= 60000:
    # Calcular el 20% sobre el valor de los ingresos
    impuesto = float(ingreso * 20 / 100)
    impuesto = round(impuesto, 2)  # Redondear a 2 decimales
    print(f"El valor del impuesto para su ingreso será de: ${impuesto}")
elif ingreso >= 60000:
    # Calcular el 10% sobre el valor de los ingresos
    impuesto = float(ingreso * 10 / 100)
    impuesto = round(impuesto, 2)  # Redondear a 2 decimales
    print(f"El valor del impuesto para su ingreso será de: ${impuesto}")
else:
    print(f"Su ingreso es inferior a 60000: ${ingreso}. No deberá abonar impuestos")

