pizza = input("Desea una pizza vegetariana o no? ")

if pizza == "si":
    ingrediente = input("Escoja uno de estos ingredientes: Pimiento o tofu ")
    print("Su pizza es vegetariana y lleva mozzarella, tomate y" ,ingrediente)
elif pizza == "no":
    ingrediente = input("Escoja uno de estos ingredientes: Peperoni, Jamón y Salmón ")
    print("Su pizza no es vegetariana y lleva mozzarella, tomate y" ,ingrediente)
