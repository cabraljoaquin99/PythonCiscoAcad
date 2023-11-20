'''
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
        # Colocar nombres y sueldos que coincidan con el operario
'''
nombres = []
sueldo_mañana = []
sueldo_tarde = []
empleados = 8
sueldo1 = 0
sueldo2 = 0

for mañana in range (4):   
    flag1 = True
    while flag1 == True:
        flag1 = False
        sueldo_str = input (f"Ingrese el sueldo del empleado numero {mañana + 1} turno mañana..\n")
        try:
            sueldo1 = float (sueldo_str)
            sueldo_mañana.append(sueldo1)
            nombre = (input ("nombre?"))
            nombres.append(nombre)
        except ValueError:
            print (f"Usted ingreso ", sueldo_str ,"es incorrecto\n, por favor, reintente con un número..")

for tarde in range (4):
    flag2 = True
    while flag2 == True:
        flag2 = False
        sueldo_str2 = input (f"Ingrese el sueldo del empleado numero {tarde + 1} turno tarde..\n")
        try:
            sueldo2 = float (sueldo_str2)
            sueldo_tarde.append(sueldo2)
            nombre = (input ("nombre?"))
            nombres.append(nombre)
        except ValueError:
            print (f"Usted ingreso ", sueldo_str2 ,"es incorrecto\n, por favor, reintente con un número..")
print ("*******************************************************")
print("Sueldos de empleados turno mañana:")
for nombre, sueldo in zip(nombres[:4], sueldo_mañana):
    print(f"{nombre}: {sueldo}")
print ("*******************************************************")
print("Sueldos de empleados turno tarde:")
for nombre, sueldo in zip(nombres[4:], sueldo_tarde):
    print(f"{nombre}: {sueldo}")
