nombre = input("Introduzca su nombre: ")
sexo = input("Introduzca su sexo(H o M): ")

if nombre[0] < "M" and sexo == "M":
    print("Perteneces al grupo A")
elif nombre[0] > "N" and sexo == "H":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")