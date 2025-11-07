numero = int(input("Introduzca un numero entero: "))
uno = int(0)
dividir = int(2)

while uno < numero:
    uno = uno +1
    resto = uno % dividir
    if resto != 0:
        print("Numero impar:" ,uno)