"""
Problema # 3
Crear una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Utilizar la función filter
"""

creditos = [
    "Libranza",
    "Libre Destino",
    "Rotativo",
    "Tarjeta de Crédito",
    "Hipotecario",
    "Carta de crédito",
]


def nombreLetra(x):
    return x[0] == "L"


filtro_creditos = filter(nombreLetra, creditos)
print(list(filtro_creditos))
print("--------")
