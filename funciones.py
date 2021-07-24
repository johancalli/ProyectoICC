# Tenemos dos tipos de funciones
# EL activar retornará un booleano
# La función tendrá el codigo y actuará en base al booleano.

# RECORDAR 1 = si, 2 = no

def activarUber():
    print("------------------------------------")
    print("FUNCION UBER")
    print("------------------------------------")
    print("¿Necesitará de un taxi para su viaje?")
    print("1. SI")
    print("2. NO")
    opcion_uber = int(input("SELECCIONA (1 o 2): "))

    while opcion_uber not in [1, 2]:
        opcion_uber = int(input("SELECCIONA (1 o 2): "))

    return opcion_uber


def activarServicios():
    pass