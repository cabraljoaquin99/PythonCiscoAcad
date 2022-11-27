my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Recorre todos los números de la lista original.
	if number not in new_list:  # Si el número no aparece dentro de la nueva lista...
		new_list.append(number)  # ...agregarlo aquí.
my_list = new_list[:]
print("La lista con elementos sin repetir: ")
print (new_list)