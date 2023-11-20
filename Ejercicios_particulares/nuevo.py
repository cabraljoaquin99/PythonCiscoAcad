'''
word_without_vowels = ""
user_word = input ("Ingrese una palabra: ")
# y asignarla a la variable user_word.
user_word = user_word.upper()
Vocales = ""
for letra in user_word:
    if letra not in Vocales == 'A' or 'E' or 'I' or 'O' or 'U':
        word_without_vowels += letra
    #

# Imprimir la palabra asignada a word_without_vowels.
print ("sin vocal ", word_without_vowels, '\n')
print ("con vocales ", user_word, '\n')
'''
word_without_vowels = ""
user_word = input("Ingrese una palabra: ")
# y asignarla a la variable user_word.
user_word = user_word.upper()
vocales = "AEIOU"
for letra in user_word:
    if letra not in vocales:
        word_without_vowels += letra
        print(word_without_vowels)
   # Completa el cuerpo del bucle.
# Imprimir la palabra asignada a word_without_vowels.
print("sin vocal ", word_without_vowels, '\n')
print("con vocales ", user_word, '\n')
