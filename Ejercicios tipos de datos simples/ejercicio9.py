cantidad = float(input("Introduzca una cantidad a invertir: "))
años = int(input("Introduzca el número de años a invertir: "))
interes = float(input("Introduce el interés anual (%): "))

capital = cantidad * (1 + interes / 100) ** años


print(f"El capital obtenido tras {años} años será de: {capital:.2f} €")