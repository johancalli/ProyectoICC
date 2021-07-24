import json


# Hay que cuidar en el caso ya estaban vacíos, solo como una función extra
def reiniciarHistorial():
    json_file = open("historial.json", "r", encoding="utf-8")
    record = json.load(json_file)
    json_file.close()

    diccionario_reinicio = {"historial": []}

    if not (record["historial"]):
        return "EL HISTORIAL YA ESTABA VACIO"
    else:
        json_file2 = open("historial.json", "w", encoding="utf-8")
        json.dump(diccionario_reinicio, json_file2, indent=4)
        json_file2.close()
        return "EL HISTORIAL HA SIDO REINICIADO"


def imprimirHistorial():
    # modificar
    json_file = open("historial.json", "r", encoding="utf-8")
    record = json.load(json_file)
    json_file.close()

    if not (record["historial"]):
        print("AUN NO HAY UN HISTORIAL")
    else:
        for i in range(len(list(record["historial"]))):
            print("------------------------------------")
            print("Busqueda " + str(i + 1))
            print("Fecha: " + str(record["historial"][i]["fecha"]))
            print("Hora: " + str(record["historial"][i]["hora"]))
            print("Punto de partida: " + record["historial"][i]["partida"])
            print("Punto de destino: " + record["historial"][i]["destino"])
            print("Ruta: " + str(record["historial"][i]["ruta"]))
