while True:
    n1 = input("Por favor, ingresa el n°1: ")
    n2 = input("Por favor, ingrese el n°2: ")

    if n1 == "" and n2 == "":
        print("¡Debe ingresar un número válido!")
    elif n1 == "":
        print("¡Debe ingresar el n°1!")
    elif n2 == "":
        print("¡Debe ingresar el n°2!")
    else:
        n1 = float(n1)
        n2 = float(n2)
        suma = n1 + n2
        print("El resultado de", n1, "y", n2, "es:", suma)
        break
