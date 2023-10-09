import re
import pandas as pd

ruta = r'C:\Users\Fabri\Documents\Tap- Bot\PRUEBAS PY\equipos2.csv'
df = pd.read_csv(ruta)

equipos = set(df['nombre'])
oracion = "cuanto 30 soles paga inter por tigres uanl inter miami cf fluminense".lower()

resultados = []


def procesar_posible_equipo(palabras):
    posible_equipo = ' '.join(palabras)
    if posible_equipo in equipos:
        return [(posible_equipo, "EQUIPO")]
    else:
        return [(palabra, '') for palabra in palabras]


palabras = re.findall(r'\b\w+\b', oracion)
i = 0
while i < len(palabras):
    palabra_actual = palabras[i]
    if palabra_actual in equipos:
        resultados.append((palabra_actual, "EQUIPO"))
        i += 1
    else:
        # Buscar grupos de palabras consecutivas que formen un equipo
        j = i + 1
        while j <= len(palabras):
            posible_equipo = palabras[i:j]
            if ' '.join(posible_equipo) in equipos:
                resultados.extend(procesar_posible_equipo(posible_equipo))
                i = j
                break
            j += 1
        else:
            # Si no se encontró un equipo, agregar la palabra tal cual
            resultados.append((palabra_actual, ''))
            i += 1

print(resultados)
