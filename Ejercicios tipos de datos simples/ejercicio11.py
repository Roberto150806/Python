dinero = float(input("Introduzca el dinero que hay en su cuenta de ahorros: "))
interes_anual = float( 4 / 100 +1 )

print( "Tienes en tu cuenta de ahorros un total de" ,dinero, "€" )

dinero_final = dinero * interes_anual
dinero_final_redondeado = round(dinero_final, 2)
dinero_final2 = dinero_final * 2
dinero_final2_redondeado = round(dinero_final2, 2)
dinero_final3 = dinero_final * 3
dinero_final3_redondeado = round(dinero_final3, 2)

print("Tus ahorros tras el primer año son de" ,dinero_final_redondeado, "€, tras tu segundo año son de" ,dinero_final2_redondeado, "€ y tras tu tercer año son de" ,dinero_final3_redondeado, "€")
