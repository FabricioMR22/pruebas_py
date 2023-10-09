import spacy
from spacy.training.example import Example
import pandas as pd

# Cargar el modelo base en español
nlp = spacy.load("es_core_news_sm")
ner = nlp.get_pipe("ner")
ner.add_label("EQUIPO")

ruta = r'C:\Users\Fabri\Documents\Tap- Bot\Service Python\Extraccion\equipos.csv'
training_data = pd.read_csv(ruta)

# Ciclo de entrenamiento
for i in range(10):  # Ajusta el número de iteraciones según tus necesidades
    for index, row in training_data.iterrows():
        text = row['nombre']
        annotations = {"entities": [(0, len(text), "EQUIPO")]}
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example])

# Guardar el modelo entrenado
nlp.to_disk("modelo_equipo")
