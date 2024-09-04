print("Bienvenido a nuestra sala de juegos ciafjuegos")
edad=int(input("Ingrese su edad: "))
if edad < 4:
    print("Ingresa gratis")
elif edad >=4 and edad < 18:
    print("El ingreso cuesta $5000")
else:
    print("El ingreso cuesta $10000")    