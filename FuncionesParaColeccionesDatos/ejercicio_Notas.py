from statistics import mean


def promedio(a, b, c, d):
    return mean([a, b, c, d])


asignaturas = [
    "Español",
    "Matemáticas",
    "Ciencias Naturales",
    "Ciencias Sociales",
    "Informatica",
]
nota_minima = 3
notas_primer_periodo = [4, 3, 2, 5, 4]
notas_segundo_periodo = [2, 5, 2, 4, 4]
notas_tercer_periodo = [1, 4, 5, 3, 5]
notas_cuarto_periodo = [3, 3, 4, 3, 4]
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
print("\nPromedio Final : {}".format(promedio_final))
print(
    "Estado Final: {}".format(
        "Aprobando" if promedio_final >= nota_minima else "Reprobando"
    )
)
