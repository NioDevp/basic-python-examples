"""En este código, te propongo unas variaciones que tendrás que crear tu para practicar
PRACTICA 1: Haz que el programa se repita en bucle hasta que se adivine el número secreto
PRÁCTICA 2: Haz que el número secreto cambie en cada partida

In this code, I suggest some variations that you will need to create yourself to practice.
PRACTICE 1: Make the program repeat in a loop until the secret number is guessed.
PRACTICE 2: Make the secret number change in each game.
"""

print("Intenta adivnar el número del 1 al 10 en el que estoy pensando")

intento_user = int(input("En que número crees que estoy pensando: "))
num_sec = 7

if intento_user == num_sec:
    print("Felicidades, el numero en el que estaba pensando era {}".format(num_sec))

print("Juego terminado")
