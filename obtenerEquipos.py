import spacy

nlp = spacy.load("es_core_news_sm")

texto = "Que tal esta pagando deportivo garcilaso"

doc = nlp(texto)

for token in doc:
    print(
        f"Palabra: {token.text}, Parte del discurso: {token.pos_}, Etiqueta: {token.tag_}")

# Analizar las entidades en el texto
for ent in doc.ents:
    print(f"Entidad: {ent.text}, Etiqueta de entidad: {ent.label_}")
