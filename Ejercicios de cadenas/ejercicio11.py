producto = input("Introduzca el nombre de un producto, su precio y un numero de unidades: ")

nombre = producto.split(",")[0]
precio = producto.split(",")[1]
unidades = producto.split(",")[2]

print (nombre,precio.zfill(6),unidades.zfill(3))
