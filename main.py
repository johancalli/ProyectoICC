import pandas as pd
import numpy as np
import networkx as nx
import graphviz
import pylab
import xlrd
import matplotlib as plt
from funciones import activarUber, activarServicios
from cadenas import puntoDestino, puntoPartida, unahoraDia, tipoDia, doshorasDia
from historial_funciones import reiniciarHistorial, imprimirHistorial
from datetime import date

while True:
    print("------------------------------------")
    print("WAZE 2.0")
    print("------------------------------------")
    print("Escoge que función deseas: ")
    print("1. Viajar")
    print("2. Historial")
    print("3. Salir")
    opcion_bienvenida = int(input("SELECCIONA (1, 2 o 3): "))

    while opcion_bienvenida not in [1, 2, 3]:
        opcion_bienvenida = int(input("SELECCIONA (1, 2 o 3): "))

    if opcion_bienvenida == 1:
        while True:
            print("------------------------------------")
            print("WAZE 2.0")
            print("------------------------------------")
            print("Escoge que tipo de busqueda deseas: ")
            print("1. Busqueda Simple")
            print("2. Busqueda Extra")
            print("3. Retroceder")
            opcion_busqueda = int(input("SELECCIONA (1, 2 o 3): "))

            while opcion_busqueda not in [1, 2, 3]:
                opcion_busqueda = int(input("SELECCIONA (1, 2 o 3): "))

            if opcion_busqueda == 3:
                break

            # Activar las funciones de uber
            # Será usado luego
            respuesta_uber = activarUber()

            # Obtener el título para el programa
            if opcion_busqueda == 1:
                titulo = "BUSQUEDA SIMPLE"
            elif opcion_busqueda == 2:
                titulo = "BUSQUEDA EXTRA"

            # Obtener el punto de partida y de destino
            partida = puntoPartida(titulo)
            destino = puntoDestino(titulo)

            # Activar saber los servicios del punto de partida y llegada
            # en caso este los tenga (CREAR un JSON para eso)
            respuesta_servicios = activarServicios()
            # Imprimir los servicios y poner un input para que no pase a lo siguiente hasta que la persona lea los servicios
            if respuesta_servicios == 1:
                serivios_espera = input("¿Listo? Para continuar precione enter: ")

            # Ahora si a trabajar las dos busquedas por separado
            if opcion_busqueda == 1:
                tipo_dia = tipoDia(titulo)  # int
                hora_dia = unahoraDia(titulo)  # int

                # Hay que obtener el dataframe
                df = pd.read_excel("estaciones.xlsx")

                metro = nx.from_pandas_edgelist(df, source='Origen', target='Destino',
                                                edge_attr='Tiempo')
                djk_path = nx.dijkstra_path(metro, source='Balbuena', target='Universidad',
                                            weight='Longitud de interestación')
                print(djk_path)

                # Vamos a obtener los valores para el dibujo
                G = nx.DiGraph()
                estaciones_origen = list(df["Origen"])
                estaciones_destino = list(df["Destino"])
                estaciones_tiempo = list(df["Tiempo"])
                for i in range(len(estaciones_origen)):
                    G.add_edges_from([(estaciones_origen[i], estaciones_destino[i])],
                                     weight=estaciones_tiempo[i])

                # Poner el camino de rojo

                # Seguir y juntar para ya hacer el dibujo

                nx.draw(G, )








            elif opcion_busqueda == 2:
                dosHoras_dia = doshorasDia(titulo)  # Esta es una lista

                # Hay que obtener el dataframe
                df = pd.read_excel("estaciones.xlsx")

            # AL ACABAR EL IF recordar guardar los datos en el inicio de la lista del historial reccordando que max pueden haber 4


    elif opcion_bienvenida == 2:
        # CREAR OTRO JSON para almacenar el historial
        # Solo se almacenaran 4 busquedas y por cada una habrá punto de partida, destino y ruta.
        while True:
            print("------------------------------------")
            print("HISTORIAL DE BUSQUEDAS")
            print("------------------------------------")
            print("Escoge que quieres hacer: ")
            print("1. Ver las ultimas busquedas")
            print("2. Borrar el historial")
            print("3. Retroceder")
            opcion_historial = int(input("SELECCIONA (1, 2 o 3): "))

            while opcion_historial not in [1, 2, 3]:
                opcion_historial = int(input("SELECCIONA (1, 2 o 3): "))

            if opcion_historial == 1:
                # Tener una función que imprima lo que está en el json
                print("------------------------------------")
                print("HISTORIAL DE BUSQUEDAS")
                print("------------------------------------")
                # Imprimimos el historial
                imprimirHistorial()
                input("Presione enter para continuar: ")

            elif opcion_historial == 2:
                # Llamamos del archivo funciones, la funcion de eliminar el historial
                print("------------------------------------")
                print("HISTORIAL DE BUSQUEDAS")
                print("------------------------------------")
                # Imprimimos la respuesta del reinicio
                print(reiniciarHistorial())
                input("Presione enter para continuar: ")

            elif opcion_historial == 3:
                break

    elif opcion_bienvenida == 3:
        break

print("")
print("------------------------------------")
print("Vuelva pronto")
print("------------------------------------")


