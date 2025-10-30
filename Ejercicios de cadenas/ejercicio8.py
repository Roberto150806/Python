
precio = input("Introduzca el precio de un producto: ")

euros = precio.split(".")[0]
centimos = precio.split(".")[1]

resultado = print("El precio es de" ,euros, "€ con" ,centimos, "centimos")