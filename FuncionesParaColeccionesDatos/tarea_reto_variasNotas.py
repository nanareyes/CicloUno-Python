"""
Crear un programa en python que muestre en pantalla el desempeño académico de un alumno en cuatro asignaturas (Español, Matemáticas, Sociales y Ciencias Naturales) al finalizar el segundo periodo del año lectivo 2021.
Se aprueba la asignatura si se obtiene una calificación mayor o igual a 3.
Se debe calcular e imprimir la calificación


"""
from colorama import init, Fore

from statistics import mean


def promedio(a, b, c, d):
    return mean([a, b, c, d])


asignaturas = ["Español", "Matemáticas", "Sociales", "Ciencias Naturales"]
nota_minima = 3
notas_primer_periodo = [4, 3, 2.5, 4]
notas_segundo_periodo = [2, 5, 2.3, 4]
notas_tercer_periodo = [2.5, 5, 1.5, 4]
notas_cuarto_periodo = [2, 3, 3, 4, 2]
"""
Uso map para invocar la función promedio a cada elemento de las listas
"""
# Promedio de los dos periodos de cada asignatura
promedioNotasAsignatura = list(
    map(
        promedio,
        notas_primer_periodo,
        notas_segundo_periodo,
        notas_tercer_periodo,
        notas_cuarto_periodo,
    )
)
promedio_final = mean(promedioNotasAsignatura)
for x in range(0, len(asignaturas)):
    print("\n asignatura: {}".format(asignaturas[x]))
    print("\n{} {}".format("Nota 1 :".ljust(14), notas_primer_periodo[x]))
    print("{} {}".format("Nota 2 :".ljust(14), notas_segundo_periodo[x]))
    print("{} {}".format("Nota 3 :".ljust(14), notas_tercer_periodo[x]))
    print("{} {}".format("Nota 4 :".ljust(14), notas_cuarto_periodo[x]))
    print("{} {}".format("Nota final :".ljust(14), promedioNotasAsignatura[x]))
    print(
        "Estado: {}".format(
            "Aprueba la asignatura"
            if promedioNotasAsignatura[x] >= nota_minima
            else "Va reprobando la asignatura"
        )
    )
    print("\n{}".format(" ".ljust(30, "=")))
init()
print("\nPromedio Final : {}".format(promedio_final))
print(
    "Estado Final: {}".format(
        Fore.YELLOW + "Aprobando"
        if promedio_final >= nota_minima
        else Fore.RED + "Reprobando"
    )
)
