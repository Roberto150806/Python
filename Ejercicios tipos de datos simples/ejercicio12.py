pan = float(3.49)
pan_nodeldia = float(3.49 * 0.60)

pan_nodeldia_vendido = int(input("Introduzca las barras que no son del dia vendidas: "))
total = pan_nodeldia_vendido * pan_nodeldia
print("Se han vendido" ,pan_nodeldia_vendido, "barras de pan que no son del día")
print("El precio habitual de una barra de pan es de" ,pan, "€, si no es del dia se le hace un descuento del 60% por lo que valdría" ,round(pan_nodeldia,2), "€, el coste total de las barras que no son del día vendidas es de" ,round(total,2))