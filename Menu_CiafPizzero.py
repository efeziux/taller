print("Bienvenido a su pizzeria ciafpizzando")

# le pedimos a nuestro cliente que solicite su pizza , si la quiere vegetariana o normal
pizza = input("Ingrese la opción de la pizza que desea, v. Vegetariana n. Normal: ")

# colocamos los ingredientes base para la ciafipiza de nuestro cliente
ingredientes_base = ["Mozzarella", "Tomate"]

if pizza == "v":
    print("Buena eleccion ciafipizero a elegido una pizza Vegetariana.")
    print("Elija porfavor un ingrediente adicional:")
    print("p. Pimiento")
    print("t. Tofu")
    
    ingre = input("Ingrese su ciapizeleccion: ")
    if ingre == "p":
        ingrediente = "Pimiento"
    elif ingre == "t":
        ingrediente = "Tofu"
    else:
        print("Opción no válida.")
        input()

elif pizza == "n":
    print("Buena eleccion ciafipizero a elegido una pizza No Vegetariana.")
    print("Elija porfavor un ingrediente adicional:")
    print("p. Peperoni")
    print("j. Jamón")
    print("s. Salmón")
    
    ingre = input("Ingrese su ciapizeleccion: ")
    if ingre == "p":
        ingrediente = "Peperoni"
    elif ingre == "j":
        ingrediente = "Jamón"
    elif ingre == "s":
        ingrediente = "Salmón"
    else:
        print("Opción no válida.")
        input()
else:
    print("Opción no válida.")
    input()

# Preguntar a  nuestro ciapizero si desea añadir mozzarella y tomate
print("¿Desea añadir Mozzarella y Tomate a su pizza?")
print("A. Sí, ambas")
print("N. No, ninguna")

normal = input("Ingrese su ciapizelección: ")

# aqui construimos  la lista de ingredientes finales de la ciafpiza
if normal == "a":
    ingredientes_finales = ingredientes_base + [ingrediente]
elif normal == "n":
    ingredientes_finales = [ingrediente]
else:
    print("Opción no válida.")
    input()

# y por ultimo Mostramos el resultado final de la eleccion de nuestro cliente
print("\n--- Resumen Final ---")
print(f"Tipo de pizza: {'Vegetariana' if pizza == 'v' else 'No Vegetariana'}")
print(f"Ingredientes: {', '.join(ingredientes_finales)}")
print("¡Gracias por su pedido!")
