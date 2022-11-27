'''
https://edube.org/learn/python-essentials-1-esp/laboratorio-hip-oacute-tesis-de-collatz-1
#HipotesisdeCollatz
Escribe un programa que lea un número natural 
y ejecute los pasos anteriores siempre que c0 
sea diferente de 1. También 
queremos que cuente los pasos necesarios para 
lograr el objetivo. Tu código también debe mostrar 
todos los valores intermedios de c0.
'''
pasos = int ()
c0= int (input ("Ingrese un num entero: "))
while c0 !=1:
#while c0 >1:
    if (c0 % 2 ==0):
        c0 = c0/2
        print (c0)
        pasos += 1
    else:
        c0 = 3 * c0 + 1
        print (c0)
        pasos += 1
print ("cantidad de pasos: ", pasos)
