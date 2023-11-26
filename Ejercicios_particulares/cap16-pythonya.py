lista = []
flag = True

while flag:
    ingreso = int(input("Ingrese un entero: "))
    lista.append(ingreso)
    if len(lista) == 5:
        flag = False

maximo = lista[0]

for elemento in lista:
    if elemento > maximo:  # Corrección aquí: comparar con 'maximo', no 'lista'
        maximo = elemento

print("El elemento mayor de la lista es:", maximo)  # Corrección aquí: no uses '=' para imprimir, usa '('
