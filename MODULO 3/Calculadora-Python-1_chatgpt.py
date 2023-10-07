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
