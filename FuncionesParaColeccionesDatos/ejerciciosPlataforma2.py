"""
problema #2
Crear una función que tome una lista de digitos y devuelva al número que corresponden. Por ejemplo [1,2,3] corresponde al número (123).
Utilizar la función reduce
"""
from functools import reduce

lista = [1, 2, 3]


def funcionNumero(acumulador, item):
    return str(acumulador) + str(item)


resultado = reduce(funcionNumero, lista)
print(resultado)
