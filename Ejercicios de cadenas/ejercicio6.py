frase = input("Introduzca una frase: ")
vocal = input("Introduzca una vocal minuscula: ")

vocalmayuscula = vocal[-1].upper()
print(frase + vocal.replace(vocal, vocalmayuscula))