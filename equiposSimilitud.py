import spacy
from fuzzywuzzy import fuzz

# Cargar el modelo de lenguaje de spaCy (debes descargarlo primero)
nlp = spacy.load("es_core_news_sm")

# Oraciones de entrada con errores ortográficos
oraciones = [
    "Cesar Vallejo gana Boca gana Alianza lima gana 30 soles cuánto paga",
    "Sasuolo gana Celta gana Argentinos jr. Gana empata 10 cuanto sale",
    "Napole gana Alianza empate visita Cristal gana Melgar gana Psv local visita Inter local empate 20",
    "Cuanto paga el Napoles gana Y el madrid gana, por 10 soles",
    "PSG gana Dortmund local visita Chicago gana empata Athetico gana Celta local visita Porto local visita A 10 cuanto sale",
    "Athetico gana PSG gana Lazio gana Dortmund gana 10 amix cuanto",
    "Sasuolo gana Celta gana Argentinos jr. Gana empata 10 cuanto sale"
]

# Lista de nombres de equipos conocidos
equipos_conocidos = ["Cesar Vallejo", "Boca", "Alianza Lima", "Sassuolo", "Celta", "Argentinos Jr.",
                     "Napoli", "Real Madrid", "PSG", "Dortmund", "Athletico Madrid", "Chicago", "Porto"]

# Umbral de similitud para considerar una palabra como un nombre de equipo
umbral_similitud = 80

# Función para encontrar el nombre de equipo más similar en la lista de equipos conocidos


def encontrar_equipo_similar(nombre_equipo):
    max_similitud = 0
    equipo_similar = None
    for equipo_conocido in equipos_conocidos:
        similitud = fuzz.ratio(nombre_equipo.lower(), equipo_conocido.lower())
        if similitud > max_similitud and similitud >= umbral_similitud:
            max_similitud = similitud
            equipo_similar = equipo_conocido
    return equipo_similar


# Procesar cada oración y encontrar nombres de equipos
for oracion in oraciones:
    doc = nlp(oracion)
    equipos = []
    for token in doc:
        # Filtrar palabras con al menos 3 caracteres
        if token.is_alpha and len(token.text) >= 3:
            nombre_equipo_similar = encontrar_equipo_similar(token.text)
            if nombre_equipo_similar:
                equipos.append(nombre_equipo_similar)
    print("Oracion:", oracion)
    print("Equipos:", equipos)
    print()
