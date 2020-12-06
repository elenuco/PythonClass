def IMC(peso,estarura):
    return peso/estatura**2
peso=float(input("Ingrese su peso"))
estatura=float(input("Ingrese su estatura"))
indice=IMC(peso, estarura)
print("Su (IMC)es: {}".format(indice))
