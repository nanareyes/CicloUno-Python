"""
La funcion map nos permite aplicar una funcion sobre cada uno de los elementos de una coleccion (listas, tuplas, etc ...).

Haremos uso de esta funcion siempre que tengamos la necesidad de transformar el valor de cada elemento en otro.

"""

# Función para doblar un número
def doblar(numero):
    return numero * 2


numeros = [2, 5, 10, 23, 50, 33]

resultado = list(map(doblar, numeros))

print(resultado)
