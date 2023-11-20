# EJEMPLO DE USO DE INDICES NEGATIVOS PARA LAS REBANADAS
'''
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
'''
#Los parámetros start y end son opcionales 
#al partir en rebanadas una lista: list[start:end], por ejemplo:

my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # salida: [3, 4, 5]
print(slice_two)  # salida: [1, 2]
print(slice_three)  # salida: [4, 5]

