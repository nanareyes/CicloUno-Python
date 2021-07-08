# Map, filter, reduce

# Map -> Función que recibe otra función para aplicársela a cada elemento de una colección
coleccion = list(range(1, 20, 3))
print("Colección :", coleccion)

# Procesos:
def decrementar(elemento):
    return elemento - 1


def incrementar5(elemento):
    return elemento + 5


def elevarCuadrado(elemento):
    return elemento ** 2


# Decrementar todos los elementos de la colección
# print(list(map(decrementar,coleccion)))
print(list(map(decrementar, coleccion)))
print(list(map(lambda elemento: elemento - 1, coleccion)))
print(list(map(incrementar5, coleccion)))
print(list(map(elevarCuadrado, coleccion)))

print("---------------------------")
# Filtrado -> predicado (función que retorna un valor booleano)
def esPar(valor):
    return valor % 2 == 0


# Solamente los pares de la colección
print(list(filter(esPar, coleccion)))


# Reduce para realizar una productoria de la colección
from functools import reduce

print(reduce(lambda acumulador=1, valor=int(): acumulador * valor, coleccion))

# Map convertir en una cadena la colección
cadena = "".join(list(map(lambda x: str(x) + " ", coleccion)))
print("Versión Cadena Colección: ", cadena, type(cadena))


# Map convertir en una cadena la colección sin repeticiones
# Insertar repeticiones
coleccion.append(4)
coleccion.append(4)
coleccion.append(19)
coleccion.append(7)
print("Antes del proceso: ", coleccion)
cadena = "".join(set(map(lambda x: str(x) + " ", coleccion)))
print("Versión Cadena Colección: ", cadena, type(cadena))

# Map convertir en una cadena la colección sin repeticiones y en orden
# Insertar repeticiones

cadena = "".join(sorted(list(set(map(lambda x: str(x) + " ", coleccion)))))
print("Versión Cadena Colección Ordenada: ", cadena, type(cadena))
