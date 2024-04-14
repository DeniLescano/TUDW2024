while True:
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
    if len(fecha) != 10 or fecha[2] != "/" or fecha[5] != "/":
        print("El formato de la fecha es incorrecto. Debe ser dd/mm/aaaa.")
    else:
        dia, mes, anio = fecha.split("/")
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print("La fecha ingresada contiene caracteres no válidos. Debe contener solo números.")
        else:
            dia = int(dia)
            mes = int(mes)
            anio = int(anio)
            if dia < 1 or mes < 1 or mes > 12 or anio < 1:
                print("La fecha ingresada no es válida.")
            elif (mes == 2 and (dia > 29 or (dia > 28 and anio % 4 != 0))) or \
                 ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30) or \
                 (dia > 31):
                print("La fecha ingresada no es válida para el mes especificado.")
            else:
                print("Día:", dia, ", Mes:", mes, "y Año:", anio)
                break
