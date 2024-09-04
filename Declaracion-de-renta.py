print(" Bienvenido le indicaremos su impositivo correspondiente segun su renta anual")

# Solicitamos al usuario que ingrese sus ingresos anuales
ingreso = int(input("Ingrese sus ingresos anuales: "))

# Evaluamos el porcentaje impositivo según los ingresos
if ingreso < 1000000:
    # Si los ingresos son menores a 1,000,000, se aplica un 5% de impuesto
    print("Su impositivo es de 5%")
elif 1000000 <= ingreso < 2000000:
    # Si los ingresos están entre 1,000,000 y 1,999,999, se aplica un 15% de impuesto
    print("Su impositivo es de 15%")
elif 2000000 <= ingreso < 3500000:
    # Si los ingresos están entre 2,000,000 y 3,499,999, se aplica un 20% de impuesto
    print("Su impositivo es de 20%")
elif 3500000 <= ingreso < 6000000:
    # Si los ingresos están entre 3,500,000 y 5,999,999, se aplica un 30% de impuesto
    print("Su impositivo es de 30%")
elif ingreso >= 6000000:
    # Si los ingresos son iguales o superiores a 6,000,000, se aplica un 45% de impuesto
    print("Su impositivo es de 45%")

