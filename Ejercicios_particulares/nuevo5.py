'''
Crear una lista y almacenar los nombres de 5 países. 
Ordenar alfabéticamente la lista e imprimirla. 
'''
lista = []
for i in range (6):
    paises = input ("Ingresar hasta 5 paises.. \n")
    paises.capitalize()
    lista.append(paises)
print ("La lista ordenada alfabeticamente.. ",sorted (lista))
