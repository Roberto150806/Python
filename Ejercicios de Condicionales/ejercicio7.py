renta_anual = int(input("Introduzca su renta anual: "))

if renta_anual < 10000:
    print("Te corresponde un tipo impositivo del 5%")
elif renta_anual >= 10000 and renta_anual <= 20000:
    print("Te corresponde un tipo impositivo del 15%")
elif renta_anual >= 20000 and renta_anual <= 35000:
    print("Te corresponde un tipo impositivo del 20%")
elif renta_anual >= 35000 and renta_anual <= 60000:
    print("Te corresponde un tipo impositivo del 30%")
elif renta_anual > 60000:
    print("Te corresponde un tipo impositivo del 45%")