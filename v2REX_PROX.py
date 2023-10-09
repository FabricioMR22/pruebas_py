import difflib
import re
import pandas as pd

ruta = r'C:\Users\Fabri\Documents\Tap- Bot\PRUEBAS PY\equipos2.csv'
df = pd.read_csv(ruta)
dictionary = set(df["nombre"])

sentence = "inter miami".lower()

words = re.findall(r'\b\w+\b', sentence)


def generate_combinations(words):
    combinations = []
    for i in range(1, min(4, len(words)) + 1):  # Hasta 3 palabras
        for j in range(len(words) - i + 1):
            current_combination = " ".join(words[j:j+i])
            # Guarda la combinación y sus posiciones
            combinations.append((current_combination, j, j + i))
    return combinations


# Inicializa un diccionario para realizar un seguimiento de las correcciones
corrections = {}

# Calcula y realiza correcciones ortográficas en la oración
combinations = generate_combinations(words)
for combination, start, end in combinations:
    best_match = difflib.get_close_matches(
        combination, dictionary, n=1, cutoff=0.85)
    if best_match:
        corrected_word = best_match[0]
        # Verifica si esta corrección está contenida en otra corrección más larga
        is_contained = False
        for (other_start, other_end), _ in corrections.items():
            if start >= other_start and end <= other_end:
                is_contained = True
                break
        if not is_contained:
            corrections[(start, end)] = corrected_word

# Aplica las correcciones a la oración
corrected_words = []
current_position = 0

for start, end in sorted(corrections.keys()):
    corrected_words.extend(words[current_position:start])
    corrected_words.append(corrections[(start, end)])
    current_position = end

corrected_words.extend(words[current_position:])
corrected_sentence = " ".join(corrected_words)

print("="*60)
print("Oracion original:", sentence)
print("Oracion corregida:", corrected_sentence)
