blocks = int(input("Ingresa el número de bloques: "))
height = 0
counter = 0

while blocks > 0:
    counter += 1
    blocks -= counter
    if blocks >= counter + 1:
        height += 1

print("La altura de la pirámide:", height)
