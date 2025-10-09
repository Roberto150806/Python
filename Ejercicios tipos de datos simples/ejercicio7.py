peso = float(input("Introduzca su peso:"))
estatura = float(input("Introduzca su altura:"))
estatura2 = estatura * estatura

imc = peso / estatura2

print(f"Tu índice de masa corporal es {imc:.2f}, donde {imc:.2f} es el índice de masa corporal calculado redondeado con dos decimales")