puntuacion = float(input("Introduzca su puntuacion: "))
dinero = int(2400)

if puntuacion == 0.0:
    dinerofinal = dinero * puntuacion
    print("Su nivel es Inaceptable")
    print("El dinero recibido será de" ,dinerofinal)
elif puntuacion == 0.4:
    dinerofinal = dinero * puntuacion
    print("Su nivel es Aceptable")
    print("El dinero recibido será de" ,dinerofinal)
elif puntuacion >= 0.6:
    dinerofinal = dinero * puntuacion
    print("Su nivel es Meritorio")
    print("El dinero recibido será de" ,dinerofinal)