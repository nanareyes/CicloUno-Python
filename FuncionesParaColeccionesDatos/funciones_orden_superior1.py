"""
FUNCIONES PARA COLECCIONES DE DATOS
Python ofrece unas funciones muy versátiles para trabajar con grandes colecciones de datos, estas son funciones de orden superior.

Las funciones más utilizadas de este tipo, para realziar operaciones sobre listas principalmente, sin ciclos, al estilo del paradigma funcional son las siguients:

+ Map
+ Reduce
+ Filter
+ Zip

----------------------------------------------------------------------------------------------------------------------------------------
Algo interesate de las funciones en Python, es que esta pueden ser asignadas a variables.
Las funciones pueden ser utilziadas como argumento de otras funciones
y pueden retornar otras funciones
----------------------------------------------------------------------------------------------------------------------------------------

"""

# Funciones de orden superior
def suma(val1, val2):
    return val1 + val2


# esta es la funcion de orden superior
def operacion(funcion, val1, val2):
    print(funcion(val1, val2))


variable_suma = suma
resultado = operacion(variable_suma, 10, 5)
print(resultado)


# Resta
def resta(val1, val2):
    return val1 - val2


variable_resta = resta
resultado = operacion(variable_resta, 10, 5)
print(resultado)

# Multiplcación
def multiplicacion(val1, val2):
    return val1 * val2


variable_multip = multiplicacion
resultado = operacion(variable_multip, 10, 5)
print(resultado)

# divisón
def division(val1, val2):
    return val1 / val2


variable_div = division
resultado = operacion(variable_div, 10, 5)
print(resultado)
