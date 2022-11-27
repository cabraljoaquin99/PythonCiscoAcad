'''
Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda 
a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes 
miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
'''
# paso 1 .. lista vacia
print("Paso 1:")
beatles = []
print(beatles)
print ("lista vacia..")
input ("Continuar al paso 2 Ingrese una tecla para continuar")
# paso 2 .. incluir metodo append
print ("Paso 2:")
beatles.append("John Lennon, ")
beatles.append("Paul McCartney, ")
beatles.append("George Harrison, ")
print(beatles)
input ("Continuar al paso 3 Ingrese una tecla para continuar")
print ("Paso 3:")
# paso 3 .. agregar a Stu Sutcliffe y Pete Best
for i in range(2):
    beatles.append(input("Nuevo miembro de la banda: "))
print("Paso 3: ,", beatles)
input ("Continuar al paso 4 Ingrese una tecla para continuar")
# paso 4 .. eliminar los dos integrantes previos
input ("Ahora, se eliminaran los integrantes 'Stu Sutcliffe y Pete Best', INGRESE UNA TECLA PARA CONTINUAR")
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)
input ("Continuar al paso 5 Ingrese una tecla para continuar")
# paso 5 .. ingreso de Ringo Starr
beatles.insert(0, 'Ringo Starr')
print("Paso 5: Nuevo integrante añadido.. \n", beatles)
# probando la longitud de la lista
print("Los Fav", len(beatles))