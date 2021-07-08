# FUNCIONES ANONIMAS
"""
Habrá ocasiones en las cuales necesitemos crear funciones de manera rápida, en tiempo de ejecución.

Funciones, las cuales realizan una tarea en concreto, regularmente pequeña.

En estos casos haremos uso de funciones lambda.
-------------------------------------------------
lambda argumento : cuerpo de la función

==================================================================
Las expresiones lambda se usan idealmente cuando necesitamos hacer algo simple y estamos más interesados en hacer el trabajo rápidamente en lugar 
de nombrar formalmente la función. Las expresiones lambda también se conocen como funciones anónimas.

Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas y anónimas (no es necesario proporcionar un nombre para las funciones 
lambda).
==================================================================
"""


def menores_10(numero):
    return numero <= 10


lista: list = [1, 2, 3, 4, 8, 9, 10, 11, 12, 14, 15, 16]

# La función de arriba se puede abreviar con lambda de la siguiente forma:
print(list(filter(lambda numero: True if numero <= 10 else False, lista)))
