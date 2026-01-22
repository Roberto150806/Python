numero = int(input("Introduce un número: "))
divisor = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisor = divisor + 1

if divisor == 2:
    print("Es primo")
else:
    print("No es primo")
