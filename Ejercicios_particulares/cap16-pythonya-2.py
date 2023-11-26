#Ingresar por teclado los nombres de 5 personas 
#y almacenarlos en una lista. Mostrar el nombre 
#de persona menor en orden alfabético.

nombres = []
t = 5

for x in range(t):
    ingreso = (input ("Ingrese los 5 nombres "))
    nombres.append (ingreso)

nombre_menor = min (nombres)

print ("El nombre de la persona menor en orden \
alfabetico es: ", nombre_menor)

