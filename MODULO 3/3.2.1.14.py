'''
https://edube.org/learn/python-essentials-1-esp/laboratorio-fundamentos-del-bucle-while

Escucha esta historia: Un niño y su padre, un programador de computadoras, 
juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara,
ya que en realidad es una pared en forma de pirámide, es plana. 
La pirámide se apila de acuerdo con un principio simple: 
cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando 
estos bloques.
Nota: La altura se mide por el número de capas completas: 
si los constructores no tienen la cantidad
suficiente de bloques y no pueden completar la siguiente capa, 
terminan su trabajo inmediatamente.
'''

bloques = int(input("Ingresa el número de bloques: "))

altura = 0
capas = 1
while capas <= bloques:
    altura += 1
    bloques -= capas
    capas += 1

print("La altura de la pirámide:", altura)
