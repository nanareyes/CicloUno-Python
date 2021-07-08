"""
Desarrolle un programa que reciba como parámetro una lista de peliculas y un caracter.

Retorne una nueva lista con las películas que empiezan con el caracter que recibe como parámetro
"""

peliculas = [
    "Mi villano favorito",
    "El castigador",
    "El principe de Persia",
    "El paseo 5",
    "Busqueda implacable",
]


def nombre_letra(x):
    return (
        "E" == x[0]
    )  #  Si está en mayúscula puede usarse . lower para buscarlo sin importar si está en mayúscula o minúscula = x[0].lower() in 'mb'


filtro_pelis = filter(nombre_letra, peliculas)
print(list(filtro_pelis))
