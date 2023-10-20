#Fahrenheit a Celsius

print(("Conversor de Grados Fahreheit (ºF) a Grados Celsius (ºC)"))
fahrenheit = float(input("Introduce los grados Fahrenheit: "))
celsius = (fahrenheit-32)*5/9
print("{} grados Fahrenheit son {} grados celsius".format(fahrenheit, celsius))