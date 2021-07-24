def puntoPartida(titulo_funcion):
    print("------------------------------------")
    print(titulo_funcion)
    print("------------------------------------")
    print("¿Cuál es su punto de partida? ")
    partida_funcion = input("ESCRIBALO: ")

    return partida_funcion


def puntoDestino(titulo_funcion):
    print("------------------------------------")
    print(titulo_funcion)
    print("------------------------------------")
    print("¿Cuál es su punto de destino? ")
    destino_funcion = input("ESCRIBALO: ")

    return destino_funcion


# Estas dos funciones son solo para la busqueda simple
def tipoDia(titulo_funcion):
    print("------------------------------------")
    print(titulo_funcion)
    print("------------------------------------")
    print("¿Qué tipo de día planeas viajar?")
    print("1. Día de Semana")
    print("2. Fin de Semana")
    print("3. Feriado")
    opcion_tipoDia = int(input("SELECCIONA (1, 2 o 3): "))

    while opcion_tipoDia not in [1, 2, 3]:
        opcion_tipoDia = int(input("SELECCIONA (1, 2 o 3): "))

    return opcion_tipoDia


def unahoraDia(titulo_funcion):
    print("------------------------------------")
    print(titulo_funcion)
    print("------------------------------------")
    print("¿En qué hora del día?")
    print("1. Mañana")
    print("2. Tarde")
    print("3. Noche")
    opcion_horaDia = int(input("SELECCIONA (1, 2 o 3): "))

    while opcion_horaDia not in [1, 2, 3]:
        opcion_horaDia = int(input("SELECCIONA (1, 2 o 3): "))

    return opcion_horaDia


# Esta funcion es solo para la busqueda extra
def doshorasDia(titulo_funcion):
    print("------------------------------------")
    print(titulo_funcion)
    print("------------------------------------")
    print("Selecciona dos horarios: ")
    print("1. Día de Semana")
    print("2. Fin de Semana")
    print("3. Feriado")
    opcion_horasDia = int(input("SELECCIONA (1, 2 o 3) y separalo por un espacio: "))

    while "," in opcion_horasDia or "  " in opcion_horasDia or "y" in opcion_horasDia and not (" " in opcion_horasDia):
        opcion_horasDia = int(input("SELECCIONA (1, 2 o 3): "))

    listaHorasDia = opcion_horasDia.split()

    return listaHorasDia

