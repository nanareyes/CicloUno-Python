# Ordenar palabras de mas o menos
txt = "but soft what light in yonder window breaks"
palabras = txt.split()
print(palabras)

l = list()

# El bucle construye una lista de tuplas, donde cada tupla es una palabra parecida por su longitud.

for subcadena in palabras:
    l.append((len(subcadena), subcadena))
print(l)

"""
La funcion sort compara el primer elemento, la longitud, primero solo considera el segundo elemento para romper los empates.
El argunmento de la palabra clave reverse=True le dice a sort que vaya en orden decreciente
"""

l.sort(reverse=True)
print(l)

# Asignación de tupla
m = ["mango", "piña"]
x, y = m
print(x)
print(y)

# Acceder a los valores de la tupla
m = ["carro", "Moto"]
x = m[0]
y = m[1]
print(x)
print(y)

# se puede hacer esto también:
m = ["televisor", "Avión"]
(x, y) = m
print(x)
print(y)

# El valor de retorno de la división es una lista con dos elementos
addr = "hugo@python.org"
usuario, dominio = addr.split("@")
print(usuario)
print(dominio)

"""
Diccionarios y tuplas
Los diccionarios tienen un método llamado elementos que devuelve una lista de tuplas, en la que cada tupla es un par clave-valor:
"""
diccionario = {"c": 10, "a": 1, "b": 22}
tupla = list(diccionario.items())
print(tupla)

# La nueva losta está ordenada en orden alfabético ascendente por el valor calve
tupla.sort()
print(tupla)
