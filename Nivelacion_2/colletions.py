# Las listas tienen una estructura al momento de escribirla, llamarla...etc, el concepto de lista permite agrupar los datos

lista = []  # Lista vacía

"""numeros = [
    58,
    57,
    25,
    56,
    37,
]  """

# para manipular los valores de las listas se hace a través de lso índices
# qué es un índice?
#            0    1   2   3   4
# numeros = [58, 57, 25, 56, 37]

# print(numeros[5]) arroja error porque no hay más indices dentro del rango de números

# Se pueden sumar, restar, multiplicar, agruparlos
# print(numeros[3] >= numeros[2])


# for -> para cada o por cada
"""
for numero in numeros:
    numero = numero ** 2
    print(numero)
"""
numeros = [58, 57, 25, 56, 37]


# numeros[1]
mensaje = "Numeros: "

for numero in numeros:
    mensaje = mensaje + str(numero) + ":"
    print(mensaje)
