while True:
    totalCuenta = input("Ingrese el precio total de la cuenta: ")
    if  totalCuenta == "":
        print("¡Debe ingresar un precio válido!")
    else:
        try:
            totalCuenta = float(totalCuenta)
        except ValueError:
            print("¡Debe ingresar un precio válido!")
        else:
            break
while True:

    cantPersonas = input("Ingrese el número de comensales: ")
    if cantPersonas == "":
        print("¡Debe ingresar un número válido!")
    else:
        try:
            cantPersonas = int(cantPersonas)
        except ValueError:
            print("¡Debe ingresar un número válido!")
        else:
            break
if cantPersonas != 0:
    montoPorPersona = totalCuenta / cantPersonas
    print("Cada persona debe pagar:", montoPorPersona)
else:
    print("No se puede dividir entre cero. ¡Debe haber al menos una persona para dividir la cuenta!")
