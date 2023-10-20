import string

text_user = input("Introduzca un texto: ")
mayusculas = 0

for letras in text_user:
    if letras in string.ascii_uppercase:
        mayusculas +=1

print("Hay {} mayusculas".format(mayusculas))
