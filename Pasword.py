#solicitamos la clave
default = "1234"
while 1:
	contra = input("Ingrese la contraseña: ")
	if contra != default:
		print("Contraseña incorrecta ¿desea intentarlo nuevamente? ")
		print("1. Si")
		print("2. No")
		selec = input()
		if selec != "2": 
			print("Ok")
		else: 
			break
	else:
		print("Bienvenido al sistema")
		break