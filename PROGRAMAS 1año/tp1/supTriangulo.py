while True:
    baseT = input("Ingrese la base del triángulo: ")
    if baseT == "":
        print("¡Debe ingresar un número válido!")
    else:
        try:
            baseT = float(baseT)
        except ValueError:
            print("¡Debe ingresar un número válido!")
        else:
            break
while True:
    alturaT = input("Ingrese la altura del triángulo: ")
    if alturaT == "":
        print("¡Debe ingresar un número válido!")
    else:
        try:
            alturaT = float(alturaT)
        except ValueError:
            print("¡Debe ingresar un número válido!")
        else:
            break
supTriangulo = (baseT * alturaT) / 2
print(f"La superficie del triángulo con base {baseT} y altura {alturaT} es: {supTriangulo}")
