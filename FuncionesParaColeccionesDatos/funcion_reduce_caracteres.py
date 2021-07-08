from functools import reduce  # es necesario importarla para poder usarla

lista = ["Python", "Java", "Ruby", "Elixir"]

resultado = reduce(
    lambda acumulador="", elemento="": acumulador + " - " + elemento, lista
)
print(resultado)
