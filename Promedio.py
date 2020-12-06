suma=0
print("\n--------Calculadora de Promedios-------------\n")
r="S"
r=(input("Digite S si desea continuar"))
while r=="S":
    respuesta=int(input("Digite la cantidad de calificaciones que desea ingresar"))
    if respuesta>=1:
        for calificaciones in range(respuesta):
            print("Nota", calificaciones+1)
            notas=float(input("Ingresa la nota"))
            suma+=notas
            if notas>=1 and notas<=10:
                promedio=suma/respuesta
            else:
                print("Digite notas Validas")
    else:
        print("\n ERROR!! Ingrese valores validos")
    print("\n Su promedio es:", promedio,"\n")
    r=(input("\nDigite S si desea continuar"))
    suma=0
else:
    print("\nAdios gracias")