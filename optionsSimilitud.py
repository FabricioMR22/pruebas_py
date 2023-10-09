import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Lista de opciones
opciones = [
    {"_id": "1", "name": "Ganador"},
    {"_id": "2", "name": "Resultado Final y DC"},
    {"_id": "3", "name": "1er Tiempo Ganador"},
]

# Preguntas
preguntas = [
    "Sasuolo gana Celta gana Argentinos jr. Gana empata 10 cuanto sale",
    "Napole gana Alianza empate visita Cristal gana Melgar gana Psv local visita Inter local empate 20",
    "Cuanto paga el Nápoles gana Y el madrid gana",
    "PSG gana Dortmund local visita Chicago gana empata Athetico gana Celta local visita Porto local visita A 10 cuanto sale",
    "Athetico gana PSG gana Lazio gana Dortmund gana 10 amix cuanto",
]

# Tokenización y preprocesamiento de texto
nltk.download('punkt')
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(
    [question.lower() for question in preguntas])
opciones_text = [opcion["name"].lower() for opcion in opciones]

# Encontrar la opción más cercana para cada pregunta
for i, pregunta in enumerate(preguntas):
    pregunta_vector = tfidf_vectorizer.transform([pregunta.lower()])
    similarities = cosine_similarity(pregunta_vector, tfidf_matrix)
    opcion_index = similarities.argmax()
    opcion = opciones[opcion_index]
    print(f"Pregunta {i+1}: {pregunta}")
    print(f"Opcion correspondiente: {opcion['name']} (ID: {opcion['_id']})")
    print("=" * 50)
