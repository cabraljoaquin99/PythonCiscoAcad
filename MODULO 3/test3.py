my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False # aqui ya entra en el bucle, 
    # pero la cond False solo es para que el programa
    # no sea infinito, asi sigue por el bucle for, abajo
    # llena la variable 'i' en una longitud igual a 'my_list' - 1
    # El algoritmo empleado es el de 
    # Ordenamiento de la burbuja: Los elementos pequeños
    # "suben" gradualmente hacia el principio de la lista
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

'''
El algoritmo utilizado en este programa es el "algoritmo de ordenamiento de burbuja" (bubble sort en inglés). 
Este algoritmo es uno de los métodos más sencillos de ordenamiento 
y funciona comparando pares de elementos adyacentes en la lista y realizando intercambios si es necesario hasta que la 
lista esté completamente ordenada.
En el código que proporcionaste:
Se crea una lista llamada my_list para almacenar los elementos que deseas ordenar.
Luego, se solicita al usuario que ingrese la cantidad de elementos que desea ordenar (num) y se pide que ingrese esos 
elementos uno por uno en la lista.
Después, se entra en un bucle while que se ejecuta hasta que no haya más intercambios necesarios en la lista. 
Inicialmente, swapped se establece en True para que el bucle se ejecute al menos una vez.
Dentro del bucle while, se itera a través de la lista y se compara cada par de elementos adyacentes. 
Si un elemento es mayor que el siguiente, se intercambian. Si se realiza un intercambio en algún momento, swapped 
se establece en True, lo que significa que el bucle debe continuar para verificar nuevamente si se requieren más 
intercambios.
Cuando no se realizan intercambios en una pasada completa a través de la lista, swapped se establece en False, 
lo que indica que la lista está completamente ordenada y el bucle while se detiene.
Finalmente, se imprime la lista ordenada.
El algoritmo de ordenamiento de burbuja puede no ser eficiente para listas muy grandes, pero es fácil de entender y es útil para 
fines educativos. Para aplicaciones prácticas en listas grandes, otros algoritmos de ordenamiento como Quicksort o Mergesort suelen 
ser más eficientes.
'''