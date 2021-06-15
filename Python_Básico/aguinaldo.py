import math

class CalculoAguinaldo:
	# Declaracion de variables 
	nombre = ""
	dui = ""
	nit = ""
	sueldo_neto = 0.00
	sueldo_diario = 0.00
	tiempo = 0
	tipo_tiempo = 0

	# Inicializamos las variables 
	def __init__(self):
		self.nombre = input("Digite el nombre del empleado: ")

		self.dui	= input("Digite el numero de DUI sin guiones: ")
		while (len(self.dui) != 9):
			self.dui	= input("Digite el numero de DUI nuevamente sin guiones: ")

		self.nit	= input("Digite el numero de NIT sin guiones: ")
		while (len(self.nit) != 14):
			self.nit	= input("Digite el numero de NIT nuevamente sin guiones: ")

		self.sueldo_neto 	= float(input("Digite el sueldo neto: "))
		self.sueldo_diario 	= self.sueldo_neto / 30
		
		self.tipo_tiempo	= int(input("Seleccione una opcion: \n 1. Años \n 2. Meses \n 3. Dias \n"))
		while ((self.tipo_tiempo < 1) and (self.tipo_tiempo > 3)):
			self.tipo_tiempo= int(input("Seleccione una opcion valida: \n 1. Años \n 2. Meses \n 3. Dias \n"))

		self.tiempo = int(input("Ingrese la cantidad de tiempo: "))

	# Calculamos el aguinaldo 
	def aguinaldo(self):
		calc_aguinaldo = 0.00
		# Definimos el tipo de calculo que se realizara en base al tipo de tiempo seleccionado
		if(self.tipo_tiempo == 1):
			calc_aguinaldo = self.calculo_anios()
		elif (self.tipo_tiempo ==2):
			calc_aguinaldo = self.calculo_meses()
		else:
			calc_aguinaldo = self.calculo_dias()

		print("El aguinaldo para ", self.nombre, "es de: $", calc_aguinaldo)
		print("-----------------------------------------------------------")
		print("El numero de DUI: ", self.dui)
		print("El numero de NIT: ",self.nit)
		print("Sueldo neto: $", self.sueldo_neto)

	def calculo_anios(self):
		if(self.tiempo >= 1 and self.tiempo < 3):
			return self.sueldo_diario * 15
		elif (self.tiempo >= 3 and self.tiempo < 10):
			return self.sueldo_diario * 19
		elif (self.tiempo >= 10):
			return self.sueldo_diario * 21

	def calculo_meses(self):
		tiempo_calc = self.tiempo / 12

		if(self.tiempo < 12):
			sueldo_calc = (self.sueldo_diario * 15) / 12
			return (sueldo_calc * self.tiempo)
		elif(tiempo_calc >= 1 and tiempo_calc < 3):
			return self.sueldo_diario * 15
		elif (tiempo_calc >= 3 and tiempo_calc < 10):
			return self.sueldo_diario * 19
		elif (tiempo_calc >= 10):
			return self.sueldo_diario * 21

	def calculo_dias(self):
		pass



print("Bienvenido al sistema de calculo de aguinaldo:")

calculo = CalculoAguinaldo()
calculo.aguinaldo()
