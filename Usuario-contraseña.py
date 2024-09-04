print("Bienvenido al concierto de las fiestas de la cosecha")
# Almacenmos la contraseña en una variable
contraseña_guardada = "Soyestudiantedeciaf2024"

# aqui pedimos al usuario que ingrese la contraseña
contraseña_usuario = input("Por favor, ingrese su contraseña: ")

# y por ultimo comparamos la contraseña ingresada con la guardada
if contraseña_usuario == contraseña_guardada:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
