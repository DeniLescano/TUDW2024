def esPalin(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
while True:
    texto = input("Ingrese un texto para verificar si es un palíndromo: ")
    if not texto:
        print("¡Debe ingresar un texto!")
    else:
        break
if esPalin(texto):
    print("El texto ingresado es un palíndromo.")
else:
    print("El texto ingresado no es un palíndromo.")
