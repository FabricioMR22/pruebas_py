import spacy

# Cargar el modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

# Preguntas de ejemplo
preguntas = [
    "Cuánto está pagando Fluminense",
    "Cuánto está pagando Inter Miami Fc",
    "Cuánto paga Tigres",
    "Sasuolo gana Celta gana Argentinos Jr  Gana empata 10 cuanto sale"
]

# Función para extraer el equipo de fútbol de una pregunta


def extraer_equipo_futbol(pregunta):
    doc = nlp(pregunta)
    equipos = []

    for ent in doc.ents:
        # Etiqueta para organización (posiblemente un equipo)
        if ent.label_ == "ORG":
            equipos.append(ent.text)

    return equipos


# Procesar las preguntas y extraer los equipos
for pregunta in preguntas:
    equipos = extraer_equipo_futbol(pregunta)
    if equipos:
        print("Equipo mencionado en la pregunta:", equipos[0])
    else:
        print("No se encontró un equipo en la pregunta")
