contraseñaguardada = ("abcd")
contraseña = input("Introduzca la contraseña: ")

if contraseña == contraseñaguardada:
    print("La contraseña introducida es correcta")
elif contraseña != contraseñaguardada:
    print("La contraseña es incorrecta")