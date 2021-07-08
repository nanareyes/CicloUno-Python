# problema # 1
"""
Utilizar la funcion incorporada map() para crear una función que retorne una lista con la longitud de cada palabra (separadas por espacios)
de una frase. La función recibe una cadena de texto y retornará una lista
"""


def longitudPalabras(frase):
    palabras = frase.split(" ")
    longitudes = list(map(len, palabras))
    return longitudes


frase = "Anita lava la tina"
print(longitudPalabras(frase))

print("......................................................")
