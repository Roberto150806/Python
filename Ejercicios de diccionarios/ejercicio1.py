diccionario =  {'Euro':'€','Dollar':'$', 'Yen':'¥'}
pregunta = input("Introduzca una divisa: ")

if pregunta in diccionario:
    print(diccionario[pregunta])
else:
    print("La divisa no esta en el diccionario")
