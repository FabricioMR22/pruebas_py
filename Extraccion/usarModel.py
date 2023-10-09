import spacy
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")

ruta = r'C:\Users\Fabri\Documents\Tap- Bot\PRUEBAS PY\equipos2.csv'
df = pd.read_csv(ruta)

nombres_equipos = df['nombre'].str.lower().tolist()  # Convertir a minúsculas


def etiquetar_equipos(texto):
    doc = nlp(texto)
    palabras_etiquetadas = []
    for token in doc:
        if token.text in nombres_equipos:
            palabras_etiquetadas.append((token.text, "EQUIPO"))
        else:
            palabras_etiquetadas.append((token.text, ""))
    return palabras_etiquetadas


# Ejemplo de uso
texto = "Cuando juega Santa Fe?"
palabras_etiquetadas = etiquetar_equipos(texto)
print(palabras_etiquetadas)
