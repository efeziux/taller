print("Bienvenido le diremos si tiene que tributar segun los siguientes requerimientos")
edad=int(input("Ingrese su edad: "))
ingresos=int(input("Ingrese sus ingresos mensuales: "))
if edad >=18 and ingresos>=3000000 :
    print("Usted debe de tributar")
else:
    print("No tiene que tributar")