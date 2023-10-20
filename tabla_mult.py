"""En este ejemplo, se muestra una versión muy básica de un programa que muestra
una pregunta al usuario para que este introduzca que tabla de multiplicar quiere ver y se la
muestra. Te animo a que intentes añadir cierta complejidad al programa, por ejemplo, dando al usuario
la opción de realizar también multiplicaciones sueltas u otra cosa que se te ocurra.

In this example, a very basic version of a program is shown, which presents a question to the user 
to input which multiplication table they want to see and then displays it. I encourage you to try 
adding some complexity to the program, for instance, by giving the user the option to also perform 
individual multiplications or any other ideas you may have."""

num_tabla = int(input("Que tabla de multiplicar desea ver: "))

for a in range (11):
    print("{} x {} = {}".format(num_tabla, a, num_tabla * a ))

