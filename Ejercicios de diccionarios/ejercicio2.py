nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca su direccion: ")
telefono = input("Introduzca su telefono: ")

diccionario =  {'Nombre':nombre,'Edad':edad,'Direccion':direccion,'Telefono':telefono}

print (diccionario['Nombre'], "tiene" ,diccionario['Edad'], "años, vive en" ,diccionario['Direccion'], "y su número de telefono es" ,diccionario['Telefono'])