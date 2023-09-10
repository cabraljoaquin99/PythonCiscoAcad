#POR COMPLETAR

#Parciales_basico = 4 --> solo aprueban con nota mayor o igual a 70%
#Parciales_intemedio = 4 --> solo aprueban con nota mayor o igual a 70%
#Finales = 2 -------> estan aprobados si su nota es igual o mas del 80%
a = "Pepe"
b = "Gustavo"
c = "Juan"
d = "Nacho"
e = "Carina"
f = "Fatima"
g = "Lucrecia"
Clases = 26
#presentes de cada alumno/a
#cuantos son regulares? > pendiente de hacer
#promedios? > pendiente de hacer
pr_a = 0
pr_b = 0
pr_c = 0
pr_d = 0
pr_e = 0
pr_f = 0
pr_g = 0
Lista_presentes = []
porcentajes_asistencia = []
resultados_pr = []
#Lista_regulaes = []
#print (type(regular_pr_a)) --------> tipo de dato
regular_pr_a = 0.0
regular_pr_b = 0.0
regular_pr_c = 0.0
regular_pr_d = 0.0
regular_pr_e = 0.0
regular_pr_f = 0.0
regular_pr_g = 0.0
for _ in range(8):
    nombre = input("Ingrese el nombre del estudiante: ")
    asistencia = int(input(f"Ingrese la asistencia de {nombre}: "))
    Lista_presentes.append(asistencia)

print(Lista_presentes)

for nombre, asistencia in zip([a, b, c, d, e, f, g], Lista_presentes):
    porcentaje_asistencia = (asistencia / Clases) * 100
    print(f"La cantidad de asistencias de {nombre} son del: {porcentaje_asistencia}%")

aprobados = 0

for asistencia in Lista_presentes:
    if asistencia >= 80:
        aprobados += 1

#print(f"La cantidad de estudiantes aprobados en finales son: {aprobados}")

#for i in Lista_presentes:
#    if i >= 80.0
