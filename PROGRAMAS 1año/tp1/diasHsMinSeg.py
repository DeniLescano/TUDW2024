while True:
    numDias = input("Ingrese el número de días: ")
    if numDias == "":
        print("¡Debe ingresar un número válido!")
    else:
        try:
            numDias = int(numDias)
        except ValueError:
            print("¡Debe ingresar un número válido!")
        else:
            break
horas = numDias * 24
minutos = horas * 60
segundos = minutos * 60
print(f"{numDias} días equivalen a:")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")
