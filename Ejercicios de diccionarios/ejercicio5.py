asignaturas = {"Matemáticas":6,"Fisica":4,"Quimica":5}
total = 0

for asig, creditos in asignaturas.items():
    print(asig, "tiene" ,creditos, "creditos")
    total = total + creditos
    
print("El total de créditos es" ,total)