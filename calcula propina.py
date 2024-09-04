#solicitmos el valor de compra al usuario
valorcompra=float(input("Porfavor ingresa el valor de la compra: "))
#Calculamos la propina del 10% del valor de la compra que ingresa nuestro usuario
propina=valorcompra * 0.10
#calculamos el total de la propina
totalpropina=valorcompra+propina
#mostramos al usuario el total de la propina
print(f"El total de la compra es: {valorcompra}")
print(f"La propina recomendada es de {propina}. El total con propina es de {totalpropina}.")




