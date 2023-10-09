import json
import requests
from fuzzywuzzy import fuzz, process


api_url = "https://api.programateapuesto.pe/api/events/?date=2023-09-19"
list_events = []
page = 1

try:
    while True:
        page_url = f"{api_url}&page={page}"
        response = requests.get(page_url)
        events = response.json()

        if page > 3:
            break

        if len(events) > 0:
            list_events.extend(events)
            page += 1
        else:
            break

except Exception as e:
    print("Error:", str(e))


def opciones_nombre_events():
    list_name_events = []
    for i in list_events:
        list_name_events.append(i["el"])
        list_name_events.append(i["ev"])
    return list_name_events


def buscarPartido(Equipo, data):
    for i in data:
        if i["el"] == Equipo or i["ev"] == Equipo:
            return "Local:", i["m"]["slct"][0]["odd"], "| Empate: ", i["m"]["slct"][1]["odd"], "| Visita", i["m"]["slct"][2]["odd"], "|", i["el"], " vs ", i["ev"]


def encontrar_similitud(cadena):
    mejor_coincidencia, puntaje = process.extractOne(
        cadena, opciones_nombre_events())
    return mejor_coincidencia


pregunta = "new casel"
resultado = buscarPartido(encontrar_similitud(pregunta), list_events)
print(resultado)
