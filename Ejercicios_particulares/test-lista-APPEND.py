'''
Definir una lista vacía 
y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.
'''
lista = []

for i in range(5) :
    valor = int (input ("Ingrese hasta 5 cargas: "))
    valor = lista.append(valor)
print ("Lista final: ", lista)
