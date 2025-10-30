cesta = input("Introduzca los productos que hay en la cesta: ")

productos =  cesta.split(",")

print (*productos, sep="\n")