"""
count()
ESte método recibe un elemento como argumento, y cuenta la cantidad de veces que aparece en la tupla.
"""
valores = ("uva", True, "Avión", 10)
print("La palabra uva aparece en la tupla: ", valores.count("uva"))

# Acceso a los elementos usando un índice negativo
frutas = ("Uva", "Lulo", "Naranja", "Mango")
frutas[-1]  # Mango

# Acceso a un subconjunto de elementos
vocales = "a", "e", "i", "o", "u"
print(vocales[2:3])  # Elementos desde el índice 2 hasta el indice 3-1(i)
vocales[2:4]  # Elementos desde el índice 2 hasta el indice 4-1(i,o)
vocales[:]  # Todos los elementos
