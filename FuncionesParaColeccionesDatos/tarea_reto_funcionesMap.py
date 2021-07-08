"""
Crear un programa en python que muestre en pantalla el desempeño académico de un alumno en dos asignaturas (Español y Matemáticas) al finalizar el segundo periodo del año lectivo 2021.
Se aprueba la asignatura si se obtiene una calificación mayor o igual a 3.
Se debe calcular e imprimir la calificación final decada asignatura y el mensaje si va aprobando o reprobando el año escolar.
"""
"""
OBSERVACION: Se debe utilizar la función map, list y mean para resolver el problema


mean() La funcion se puede usar para calcular la media / promedio de una lsita de numeros dada, devuelve la media del conjunto de datos pasando como
perámetros.
La media aritmética es la suma de datos dividica por el número de puntos de datos.

El Módulo statistics viene con la función mean
"""

from statistics import mean


def promedio(a, b):
    return mean([a, b])


asignaturas = ["Español", "Matemáticas"]
nota_minima = 3
notas_primer_periodo = [4, 3]
notas_segundo_periodo = [2, 5]
"""
Uso map para invocar la función promedio a cada elemento de las listas
"""
# Promedio de los dos periodos de cada asignatura
promedioNotasAsignatura = list(
    map(promedio, notas_primer_periodo, notas_segundo_periodo)
)
promedio_final = round(mean(promedioNotasAsignatura), 2)
for x in range(0, len(asignaturas)):
    print("\n asignatura: {}".format(asignaturas[x]))
    print("\n{} {}".format("Nota 1 :".ljust(14), notas_primer_periodo[x]))
    print("{} {}".format("Nota 2 :".ljust(14), notas_segundo_periodo[x]))
    print("{} {}".format("Nota final :".ljust(14), promedioNotasAsignatura[x]))
    print(
        "Estado: {}".format(
            "Aprueba la asignatura"
            if promedioNotasAsignatura[x] >= nota_minima
            else "Va reprobando la asignatura"
        )
    )
    print("\n{}".format(" ".ljust(30, "=")))
print("\nPromedio Final : {}".format(promedio_final))
print(
    "Estado Final: {}".format(
        "Aprobando" if promedio_final >= nota_minima else "Reprobando"
    )
)
