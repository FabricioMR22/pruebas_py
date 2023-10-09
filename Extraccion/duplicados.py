import pandas as pd

ruta = r'C:\Users\Fabri\Documents\Tap- Bot\Service Python\equipos2.csv'
mi_dataframe = pd.read_csv(ruta)

# Verificar duplicados en la columna 'nombre'
duplicados = mi_dataframe[mi_dataframe.duplicated(subset='nombre', keep=False)]

if not duplicados.empty:
    print("Hay elementos duplicados en la columna 'nombre':")
    print(duplicados)
else:
    print("No se encontraron elementos duplicados en la columna 'nombre'.")


elemento_a_buscar = "Sasuolo".lower()

# Usando el método loc
fila = mi_dataframe.loc[mi_dataframe['nombre'] == elemento_a_buscar]

if not fila.empty:
    print("La fila que contiene '{}' en la columna 'nombre' es:".format(
        elemento_a_buscar))
    print(fila)
else:
    print("No se encontró el elemento '{}' en la columna 'nombre'.".format(
        elemento_a_buscar))
