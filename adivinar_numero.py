print("Intenta adivnar el número del 1 al 10 en el que estoy pensando")

intento_user = int(input("En que número crees que estoy pensando: "))
num_sec = 7

if intento_user == num_sec:
    print("Felicidades, el numero en el que estaba pensando era {}".format(num_sec))

print("Juego terminado")
