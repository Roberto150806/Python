edad = int(input("Introduzca su edad: "))
ingresos = int(input("Introduzca sus ingresos mensuales: "))

if edad < 16 or ingresos < 1000:
    print("No debe tributar")
elif edad > 16 and ingresos >= 1000:
    print("Debe tributar")