'''
Pedir al usuario que ingrese una palabra.
Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de 
la palabra ingresada.
Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.
Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. 

Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga 
durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.
'''
# Indicar al usuario que ingrese una palabra
# y asignarla a la variable 'letras'
palabra = input ("ingrese una palabra aquí: ")
palabra= palabra.upper()
words_without_vowels = ""

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
    words_without_vowels= words_without_vowels + letras
print (words_without_vowels, "\n")

   # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.