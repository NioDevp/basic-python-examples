#CONVERSOR DIVISAS
#El factor de conversión puede variar con el tiempo/ The convesion factor can change over time

dolar_euro = 0,90
euro_dolar = 1,11
libra_euro = 1.17
euro_libra = 0.86

mode = input("¿Que conversión quiere hacer?\n"
             "A - Dolar a Euro\n"
             "B - Euro a Dolar\n"
             "C - Libra a Euro\n"
             "D - Euro a Libra\n")

if mode == "A":
    dolar = float(input("Introduzca la cantidad de dolares que quiere convertir a euros: "))
    print("{} dolares son {} euros".format(dolar, dolar * dolar_euro))
elif mode == "B":
    euro = float(input("Introduzca la cantidad de euros que quiere convertir a dolares: "))
    print("{} euros son {} dolares".format(euro, euro * euro_dolar))
elif mode == "C":
    libra = float(input("Introduzca la cantidad de libras que quiere convertir a euros: "))
    print("{} libras son {} euros".format(libra, libra * libra_euro))
elif mode == "D":
    euro = float(input("Introduzca la cantidad de euros que quiere convertir a libras:"))
    print("{} euros son {} libras".format(euro, euro * euro_libra))
else:
    print("Selecciones una opción válida")
