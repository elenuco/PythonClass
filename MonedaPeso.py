#solicitamos valores
print("Por favor Ingrese el número de la selección deseada:")
print("1. Convertir libras a kilos")
print("2. Convertir kilos a libras")
print("3. Convertir EUR a USD")
print("4. Convertir USD a EUR")

selec=int(input())

#procesamos la info
if selec == 1:
	lb = float(input("Ingrese la cantidad de libras: "))
	kg = lb * 0.45359237
	print("Son {}kg.".format(kg))
elif selec == 2:
	kg = float(input("Ingrese la cantidad de kilogramos: "))
	lb = kg / 0.45359237
	print("Son {}lb.".format(lb))
elif selec == 3 or selec == 4:
	TC = float(input("Ingrese el Tipo de cambio actual (EUR/USD): "))
	if selec == 3:
		EUR = float(input("Ingrese la cantidad de EUR: "))
		USD = EUR * TC
		print("Son {}USD.".format(USD))
	else:
		USD = float(input("Ingrese la cantidad de USD: "))
		EUR = USD / TC
		print("Son {}EUR.".format(EUR))
else: print("Intentelo nuevamente.")