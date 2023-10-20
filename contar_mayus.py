import string

texto_user = input("Introduzca un texto: ")
mayusculas = 0

for letras in texto_user:
    if letras in string.ascii_uppercase:
        mayusculas +=1

print("Hay {} mayusculas".format(mayusculas))