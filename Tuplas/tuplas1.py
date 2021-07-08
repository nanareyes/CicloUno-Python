"""
TUPLAS
Una tupla es una secuenccia de valores muy parecida a una lista.
Los valores almacenados en una tupla pueden ser de cualquier tipo, y están indexados por números enteros.
La diferencia importante es que las tuplas son inmutables.
Una tupla es una lista de valores separada por comas
"""

t = "a", "b", "c", "d", "e"
print(t)  # imprimir tupla

t = "1", "2", "3", "4", "5"
print(t)

t = 3, "a", 8, 7.2, "hola"
print(t)

t = ("esto es una cadena", "b", "c", "d", "e")
print(t)

"""
Si el argumento es una secuencia (cadena, lsita o tupla), el resultado de la llamada a la tupla es una tupla con los elementos de la secuencia:
"""

t = tuple("lupines")
print(t)  # Resultado : ('l', 'u', 'p', 'i', 'n', 'e', 's')

"""
Si intentas modificar uno de lo selementos de la tupla, obtienes un error
"""

t = "a", "b", "c", "d", "e"
t[0] = "x"

# comparando tuplas
(0, 3, 4) < (0, 2, 2)  # false
(0, 1, 1) < (0, 3, 4)  # true

# original Tuple + (newElement,)
tupla = (1, 2, 3)
tupla = tupla + (1,)
print(tupla)
