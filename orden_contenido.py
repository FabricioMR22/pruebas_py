import difflib
import pandas as pd


def custom_similarity(word1, word2):
    # Similitud basada en el orden de las letras
    order_similarity = difflib.SequenceMatcher(None, word1, word2).ratio()

    # Similitud basada en las letras contenidas
    set1 = set(word1)
    set2 = set(word2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        letter_similarity = 0
    else:
        letter_similarity = intersection / union

    # Pondera las dos similitudes y calcula un porcentaje final
    weight_order = 0.95  # Puedes ajustar estos pesos según tus preferencias
    weight_letter = 0.05
    final_similarity = (order_similarity * weight_order) + \
        (letter_similarity * weight_letter)

    return final_similarity


word_to_check = "apoel"
ruta = r'C:\Users\Fabri\Documents\Tap- Bot\PRUEBAS PY\equipos2.csv'
df = pd.read_csv(ruta)
possibilities = set(df["nombre"])
# possibilities = ["chau", "hola", "ho", "h"]

best_matches = sorted(possibilities, key=lambda x: custom_similarity(
    word_to_check, x), reverse=True)

print(best_matches)
