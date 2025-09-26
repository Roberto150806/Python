peso = float(input("Introduzca su peso: "))
altura = float(input("Introduzca su altura: "))
altura2 = altura * altura

imc = peso / altura2
print(f"Tu índice de masa corporal es {imc:.2f}, donde {imc:.2f} es el índice de masa corporal calculado redondeado con dos decimales")
