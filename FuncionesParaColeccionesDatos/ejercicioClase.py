"""
1. Crear una función que determine el equipo de futbol, cuyo nombre inicie con la letra “T”, utilizar la función map para iterar en la lista equipos.

equipos = ["América", "Millonarios", "Tolima", "Cali", "Junior"]  

Generar una lista de resultado que indique con true los nombres que inicien con 

la letra “T” y false para los que no cumplan la condición. 
La lista generada es la siguiente:
[False, False, True, False, False]


"""

equipos = ["America", "Millonarios", "Tolima", "Cali", "Junior"]


def nombre_equipo(x):
    if x[0] == "T":
        return True
    else:
        return False


result = list(map(nombre_equipo, equipos))

print(result)
