'''
1- Presentar un menu de opciones
	CALCULADORA EN PYTHON
	Suma
	Resta
	Multiplicacion
	Division
	Potencia
2- Solicitar al usuario, ingrese una opción:
	Ingrese una opción a realizar: _
3- Solicite al usuario "ingrese dos operandos:"
4- Realizar la operación seleccionada.
5- Presentar el resultado.

'''
Lsuma= []
Lresta= []
Lmultip= []
Ldiv= []
Lpot = []
#calculadora, suma, resta, multip, div, pot = 0 (int)
#totalsuma, totalresta, totalmultip, totaldiv, totalpot = 0
print(
"""
+==================================+
| Ingrese una opción a realizar:   |
| 1: Suma                          |
| 2: Resta        				   |
| 3: Multiplicación                |
| 4: División					   |
| 5: Potencia					   |
| 6: Salir de la calculadora	   |
+==================================+
""")
calculadora = int (input (""))
if (calculadora == 1):
	suma = 6
	for i in range (2):
		while suma >= 2:
			Lsuma[0] = int (input ("Ingrese solo dos operandos: \n"))
			#Lsuma [0] = suma
			suma = int (input ("Ingrese el último: "))
			suma = Lsuma [1]
			totalsuma = Lsuma [0] + Lsuma [1]
			print (totalsuma)
		suma -= 3
elif (calculadora == 2):
	resta = 6
	for i in range (2):
		while resta >= 2:
			resta = int (input ("Ingrese solo dos operandos \n"))
			resta = Lresta [0]
			resta = int (input ("Ingrese el último: "))
			resta = Lresta [1]
			totalresta = Lresta [0] - Lresta [1]
			print (totalresta)
		resta -= 3
elif (calculadora == 3):
	multip = 6
	for i in range (2):
		while multip >= 2:
			multip = int (input ("Ingrese solo dos operandos \n"))
			multip = Lmultip [0]
			multip = int (input ("Ingrese el último: "))
			multip = Lmultip [1]
			totalmultip = Lmultip [0] * Lmultip [1]
			print (totalmultip)
		multip -= 3
elif (calculadora == 4):
	div = 6
	for i in range >= 2:
		while div >= 2:
			div = int (input ("Ingrese solo dos operandos \n"))
			div = Ldiv [0]
			div = int (input ("Ingrese el último: "))
			div = Lmultip [1]
			totalmultip = Lmultip [0] + Lmultip [1]
			print (totalmultip)
		div -= 3
elif (calculadora == 5):
	pot = 6
	for i in range >= 2:
		while pot >= 2:
			pot = int (input ("Ingrese solo dos operandos \n"))
			pot = Lpot [0]
			pot = int (input ("Ingrese el último: "))
			pot = Lpot [1]
			totalpot = Lpot [0] * Lpot [1]
			print (totalpot)
		pot -= 3
else:
	print ("Cierre del programa, saliendo...")

'''
El código que has compartido tiene varios errores. Aquí te explico los problemas y cómo corregirlos:

1. En Python, no es necesario declarar explícitamente el tipo de variables, como lo has hecho en estas líneas:

   ```python
   calculadora, suma, resta, multip, div, pot = 0 (int)
   totalsuma, totalresta, totalmultip, totaldiv, totalpot = 0
   ```

   Puedes simplemente inicializar las variables sin especificar el tipo de dato.

2. En las condiciones dentro de los bloques `if`, debes comparar con valores enteros en lugar de números sin comillas, ya que las opciones del menú son enteros:

   ```python
   if calculadora == 1:
   ```

   Además, debes convertir la entrada del usuario a un entero usando `int()`, ya que `input()` devuelve una cadena de caracteres.

3. El uso de `==` se utiliza para comparar igualdad, pero en tu código, estás utilizando `==` en lugar de `=` para asignar valores. Por ejemplo:

   ```python
   suma == 6
   ```

   Debe ser:

   ```python
   suma = 6
   ```

4. El bucle `for` que usas en cada operación no tiene sentido y complica innecesariamente tu código. No necesitas un bucle `for` para solicitar dos operandos.

5. Las variables `Lsuma`, `Lresta`, etc., están definidas como listas vacías, pero luego intentas asignarles valores directamente sin agregar elementos a la lista primero.

6. Los bloques `if` deberían estar dentro de un bucle mientras el usuario no elija la opción "Salir".

Aquí tienes una versión corregida y simplificada de tu código:

```python
while True:
    print(
    """
    +==================================+
    | Ingrese una opción a realizar:   |
    | 1: Suma                          |
    | 2: Resta        				   |
    | 3: Multiplicación                |
    | 4: División					   |
    | 5: Potencia					   |
    | 6: Salir de la calculadora	   |
    +==================================+
    """)
    
    calculadora = int(input())
    
    if calculadora == 1:
        operandos = [float(input("Ingrese el primer operando: ")), float(input("Ingrese el segundo operando: "))]
        resultado = sum(operandos)
        print("Resultado de la suma:", resultado)
    elif calculadora == 2:
        operandos = [float(input("Ingrese el primer operando: ")), float(input("Ingrese el segundo operando: "))]
        resultado = operandos[0] - operandos[1]
        print("Resultado de la resta:", resultado)
    elif calculadora == 3:
        operandos = [float(input("Ingrese el primer operando: ")), float(input("Ingrese el segundo operando: "))]
        resultado = operandos[0] * operandos[1]
        print("Resultado de la multiplicación:", resultado)
    elif calculadora == 4:
        operandos = [float(input("Ingrese el primer operando: ")), float(input("Ingrese el segundo operando: "))]
        if operandos[1] == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = operandos[0] / operandos[1]
            print("Resultado de la división:", resultado)
    elif calculadora == 5:
        operandos = [float(input("Ingrese el primer operando: ")), float(input("Ingrese el segundo operando: "))]
        resultado = operandos[0] ** operandos[1]
        print("Resultado de la potencia:", resultado)
    elif calculadora == 6:
        print("Cierre del programa, saliendo...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
```

Este código solicita operaciones y operandos dentro de un bucle mientras el usuario no elija salir, y maneja las operaciones de acuerdo a la elección del usuario.
'''