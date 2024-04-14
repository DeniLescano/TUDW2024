while True:
    texto = input("Ingrese una cadena de texto: ")
    if not texto:
        print("¡Debe ingresar un texto!")
    else:
        primCincoLetras = ""
        contador = 0
        for char in texto:
            if char != " ":
                primCincoLetras += char
                contador += 1
            if contador == 5:
                break
        print("Los primeros 5 caracteres del texto son:", primCincoLetras)
        break

