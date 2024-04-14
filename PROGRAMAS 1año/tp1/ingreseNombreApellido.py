while True:
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Por favor, ingrese tu apellido: ")

    if nombre == "" and apellido == "":
        print("¡Debe ingresar un nombre y un apellido!")
    elif nombre == "":
        print("¡Debe ingresar un nombre!")
    elif apellido == "":
        print("¡Debe ingresar un apellido!")
    else:
        print("El nombre y apellido ingresados son:", nombre, apellido)
        break
