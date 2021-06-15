#Nombre del empleado y horas laborales
nombre=input("Nombre del empleado")
DUI=input("Ingrese Su DUI:")
NIT=input("Ingrese su su NIT:")
salario=float(input("Digite su salario:"))
confirmacion_bono=input("¿  Tienes un bono?\n 1.Si \n 2.No")
if confirmacion_bono=="1":
    float("Ingrese la cantidad de bono: ")
if confirmacion_bono=="2":
    bono=0
#descuentos de ley
AFP=salario*0.0725
ISSS=salario*0.03
retenciones= ISSS+AFP
neto=salario-retenciones
print("Su retencion del ISSS es:", ISSS)
print("Su retencion del AFP es:", AFP)
print("Su retencion total es:", retenciones)
print("Su salario neto:", neto)
#dwscuento de la renta
if neto<=472.00:
    print("Su salaeio no aplica a la retencion de la renta")
elif neto >=472.01 and neto<=895.24:
    renta=neto*0.10
    print("Su Salario aplica a la retencion, su descuento es de ", renta)
    descuento=neto-renta
    final=descuento+bono
    print(nombre,"\n", DUI,"\n",NIT,"\n","Su salario final es:", "\n",final)
