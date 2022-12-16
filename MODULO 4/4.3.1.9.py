'''
Escribir una función que verifique si un número es primo o no.

Funcion es llamada 'is_prime'.
Toma un argumento (el valor a verificar).
Devuelve True si el argumento es un número primo, 
y False de lo contrario.
'''
def is_prime(num):
  if num <= 1:
    return False

  for i in range(2, num):
    if num % i == 0:
      return False

  return True


# Pedir al usuario que ingrese un número
ingreso = input("Escriba un número entero: ")

# Convertir la cadena ingresada por el usuario a entero
num = int(ingreso)

# Verificar si el número es primo
resultado = is_prime(num)

# Imprimir el resultado
print(resultado)