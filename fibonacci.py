"""En este código se hace uso de funciones para imprimir por pantalla la secuencia de 
Fibonacci. Como práctica, te animo a mejorar la interacción con el usuario final añadiendo, por
ejemplo, un mensaje al principio del programa.

In this code, functions are used to print the Fibonacci sequence to the screen. As an exercise,
I encourage you to enhance the interaction with the end user by, for instance, adding a message 
at the beginning of the program."""

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    for a in range(10):
        print(fibonacci(a))


if __name__ == "__main__":
    main()
