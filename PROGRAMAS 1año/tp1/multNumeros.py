while True:
    n1 = input("Por favor, ingresa el primer número: ")
    n2 = input("Por favor, ingresa el segundo número: ")
    n3 = input("Por favor, ingresa el tercer número: ")
    if n1 == "" or n2 == "" or n3 == "":
        print("¡Debe ingresar tres números válidos!")
    else:
        try:
            n1 = float(n1)
            n2 = float(n2)
            n3 = float(n3)
        except ValueError:
            print("¡Debes ingresar números válidos!")
        else:
            resultado = (n1 + n2) * n3
            print("La respuesta es", resultado)
            break
