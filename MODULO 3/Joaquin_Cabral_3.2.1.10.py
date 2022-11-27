#from distutils.command.config import config

palabra= input ("Ingresar una palabra aquí: ")
palabra= palabra.upper ()

for letras in palabra:
    if letras == "A":
        continue
    if letras == "E":
        continue
    if letras == "I":
        continue
    if letras == "O":
        continue
    if letras == "U":
        continue
    else:
        print (letras)
