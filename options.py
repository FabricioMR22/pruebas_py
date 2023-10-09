import json


archivo_json = "data.json"

with open(archivo_json, "r") as archivo:
    data = json.load(archivo)

valores_deb = []

for objeto in data["m"]:
    valores_deb.append(objeto["deb"])
print(valores_deb.__len__())

opciones_lista = [{"_id": str(i), "name": valor}
                  for i, valor in enumerate(valores_deb, start=1)]

# Especifica la ruta donde deseas guardar el archivo JSON
archivo_json = "opciones.json"  # Reemplaza con la ruta de tu elección

# Guarda la lista de diccionarios en el archivo JSON
with open(archivo_json, "w") as archivo:
    json.dump(opciones_lista, archivo, indent=2)

# Imprime el JSON creado
print(f"Archivo JSON creado: {archivo_json}")
