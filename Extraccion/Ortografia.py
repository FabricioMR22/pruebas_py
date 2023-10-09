from transformers import BertTokenizer, BertForMaskedLM, pipeline

# Carga un modelo BERT preentrenado en español que no requiere autorización
tokenizer = BertTokenizer.from_pretrained(
    "dccuchile/bert-base-spanish-wwm-cased")
model = BertForMaskedLM.from_pretrained(
    "dccuchile/bert-base-spanish-wwm-cased")

# Resto del código sin cambios


# Crea un pipeline para reemplazar [MASK] con la corrección sugerida
fill_mask = pipeline(
    "fill-mask",
    model=model,
    tokenizer=tokenizer
)

# Define una función para corregir ortografía en una oración


def corregir_ortografia_oracion(oracion):
    tokens = oracion.split()
    nueva_oracion = []
    for token in tokens:
        if token.lower() == "ral":
            correccion = fill_mask(token.lower() + " <mask>")
            nueva_oracion.append(correccion[0]['token_str'])
        else:
            nueva_oracion.append(token)
    return ' '.join(nueva_oracion)


# Ejemplo de corrección ortográfica en una oración
oracion = "Hoy juega el [MASK] madrid"
correccion = fill_mask(oracion)

oracion_corregida = corregir_ortografia_oracion(oracion)
print(f'Oración original: {oracion}')
print(f'Oración corregida: {correccion}')
