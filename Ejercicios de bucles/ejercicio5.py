invertir = int(input("Introduzca una cantidad a invertir: "))
interes = float(input("Introduzca el interés anual en decimal: "))
años = int(input("Introduzca cuantos años: "))
contador = int(0)
contar_año = int(0)

while años > contador:
    invertir = invertir * interes
    años = años - 1
    contar_año = contar_año + 1
    print("Año" ,contar_año, ":" ,invertir)