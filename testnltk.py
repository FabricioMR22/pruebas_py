import spacy
from unidecode import unidecode

# Cargar el modelo pre-entrenado en español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo en español
texto = "Cuanto paga el Nápoles gana Y el madrid gana, por 10 soles"
texto = unidecode(texto).lower()

# Procesar el texto con SpaCy
doc = nlp(texto)

# Etiquetar palabras
for token in doc:
    print(token.text, token.pos_)
