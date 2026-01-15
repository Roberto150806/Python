dfrutas = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
preguntafruta = input("Que fruta va a escoger: ")


if preguntafruta in dfrutas:
    kilos = int(input("Cuantos kilos va a coger: "))
    calculo = dfrutas[preguntafruta] * kilos
    print ("El precio es" ,calculo, "€")

else:
    print("La fruta no esta en el diccionario")