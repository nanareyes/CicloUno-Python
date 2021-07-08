# Cadenas -> Flujos de caracteres o palabras (orden inmutables)
cadena = "hola Mundo"
print(cadena[0])
print(cadena[-1])
print(cadena[2])
print(cadena[0:4])

# las cadenas son inmutables, pero se pueden reordenar a partir de caracteres
cadena = cadena[0].upper() + cadena[1:]  # upper para mayúscula
print(cadena)

# Listas -> obedecen a un orden también se pueden modificar (mutables)
lista = [12, "hola", "casa", 45]
print(lista[0])
print(lista[-1])
print(lista[0:2])
lista[0] = 24  # Las listas son mutables y permiten insercciones
print(lista)
lista.append("nuevo elemento")  # agrega un nuevo elemento al final
print(lista)
lista.insert(0, [6, 7, 8])  # insterta lista en el primer espacio (0)
print(lista)
lista.pop(0)  # decrementar la lista, si no se especifica: elimina el último
print(lista)
"""si no queremos coleccionar elementos que se modifiquen escogemos tuplas, pero de lo contrario escogemos listas"""

# Tuplas -> equivalentes a listas que no se pueden modificar
a = 12
b = 12
tupla = (a, b, lista)
print(tupla)

# Las tuplas van con paréntesis redondos

# No siguen un orden -> conjutnos, diccionarios

# Conjuntos
conjunto = {"Armenia", "Bogotá", "Cali"}
for elemento in conjunto:
    print(elemento)
print("--------------")
conjunto.add("Ibagué")  # para agregar un elemento
conjunto.remove("Armenia")  # para remover
for elemento in conjunto:
    print(elemento)
