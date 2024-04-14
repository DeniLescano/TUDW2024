while True:
    nombre = input("Ingrese su nombre: ")
    if not nombre or not nombre.replace(" ", "").isalpha():
        print("¡Nombre inválido! Debe contener solo letras y no estar vacío.")
    else:
        break
while True:
    apellido = input("Ingrese su apellido: ")
    if not apellido or not apellido.replace(" ", "").isalpha():
        print("¡Apellido inválido! Debe contener solo letras y no estar vacío.")
    else:
        break
while True:
    anioNac = input("Ingrese su año de nacimiento: ")
    if not anioNac or not anioNac.isdigit():
        print("¡Año de nacimiento inválido! Debe ser un número y no estar vacío.")
    else:
        break
usuario = nombre[0].lower() + apellido.replace(" ", "").lower()
contrasenia = usuario + "." + anioNac
print("Usuario:", usuario)
print("Contraseña:", contrasenia)
