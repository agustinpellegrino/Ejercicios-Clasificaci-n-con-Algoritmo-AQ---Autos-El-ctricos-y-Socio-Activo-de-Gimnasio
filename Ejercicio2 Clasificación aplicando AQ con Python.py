# Paso 1: Ejemplos positivos

positivos = [
    {"edad": 25, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 32, "frecuencia": "frecuente", "plan": "premium"},
    {"edad": 45, "frecuencia": "frecuente", "plan": "premium"}
]

# Paso 2: Ejemplos negativos

negativos = [
    {"edad": 25, "frecuencia": "ocasional", "plan": "basico"},
    {"edad": 32, "frecuencia": "ocasional", "plan": "estandar"},
    {"edad": 38, "frecuencia": "rara", "plan": "basico"}
]

# Paso 3: Inducción de reglas

regla = {}

atributos = []

ejemplo = positivos[0]

for clave in ejemplo:
    atributos.append(clave)

for atributo in atributos:

    valores_pos = []
    valores_neg = []

    # Valores de los ejemplos positivos
    for ej in positivos:
        valor = ej[atributo]

        if valor not in valores_pos:
            valores_pos.append(valor)

    # Valores de los ejemplos negativos
    for ej in negativos:
        valor = ej[atributo]

        if valor not in valores_neg:
            valores_neg.append(valor)

    # Buscar valores exclusivos de los positivos
    valores_validos = []

    for valor in valores_pos:

        encontrado = False

        for v in valores_neg:

            if valor == v:
                encontrado = True
                break

        if not encontrado:
            valores_validos.append(valor)

    if len(valores_validos) > 0:
        regla[atributo] = valores_validos


# Paso 4: Mostrar regla inducida

print("Regla inducida para identificar a un Socio Activo:")

for atributo in regla:
    print("-", atributo, "=", regla[atributo])


# Paso 5: Regla SI - ENTONCES

print("\nRegla de clasificación:")

for atributo in regla:
    for valor in regla[atributo]:
        print("SI", atributo, "=", valor)

print("ENTONCES Socio_Activo = Sí")