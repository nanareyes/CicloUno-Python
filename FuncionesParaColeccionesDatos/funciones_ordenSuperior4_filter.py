# Funcion Filter ()
# Filtra unos elementos de una lista determinada a partir de una condición
"""
Tal como su nombre indica filter significa filtrar, y es una de mis 
funciones favoritas, ya que a partir de una lista o iterador y una 
función condicional, es capaz de devolver una nueva colección con 
los elementos filtrados que cumplan la condición.

"""


def multiplo_cinco(numero):
    if numero % 5 == 0:
        return True


numeros = [2, 5, 10, 23, 50, 33]
resultado = list(filter(multiplo_cinco, numeros))
print(resultado)
