def inversion(Capital, interes_anual, plazo):
   return Capital*interes_anual*plazo
Capital=float(input("Capital a invertir (c)"))
interes_anual=float(input("Interes anual (i)"))
plazo=float(input("Ingrese el plazo o el anio (t)"))
capital_total=inversion(Capital, interes_anual, plazo)
print("Sucapital total es: {}".format(capital_total))