# Este es el ejerc de tarea:

"""
En una universidad se desea conocer el promedio de calificaciones de la asignatura Matemática I de la carrera de Ingeniería Civil, el programa 
cuenta con tres grupos, se necesita calcular el promedio de calificaciones del primer parcial por cada grupo y el promedio de calificaciones a 
nivel general, por otra parte, se necesita conocer el número de alumnos de cada grupo y el total general.

Se debe procesar n cantidad de datos de los estudiantes con la siguiente información:
1. Código grupo
2. Calificación 

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
Código_grupo: Puede ser 01, 02 y 03
calificacion: int

Ejemplo Datos
datos: list = [
    {   "cod_grupo": "01",
        "calificacion": 5     },
    {   "cod_grupo": "02",
        "calificacion": 2     },
    {   "cod_grupo": "01",
        "calificacion": 3     },
]

La respuesta debe retornar un diccionario con la siguiente información:

Promedio Calificaciones del programa
Promedio calificaciones grupo 01
Promedio calificaciones grupo 02
Promedio calificaciones grupo 03
# de alumnos grupo 01
# de alumnos grupo 02
# de alumnos grupo 03
# de alumnos matriculados en Matemática I

"""
datos: list = [
    {"cod_grupo": "01", "calificacion": 5},
    {"cod_grupo": "02", "calificacion": 2},
    {"cod_grupo": "03", "calificacion": 3},
    {"cod_grupo": "01", "calificacion": 3.5},
    {"cod_grupo": "02", "calificacion": 2.5},
    {"cod_grupo": "03", "calificacion": 3.5},
    {"cod_grupo": "01", "calificacion": 2},
    {"cod_grupo": "03", "calificacion": 3},
    {"cod_grupo": "01", "calificacion": 4},
    {"cod_grupo": "03", "calificacion": 3.5},
    {"cod_grupo": "02", "calificacion": 2.5},
    {"cod_grupo": "01", "calificacion": 4.5},
    {"cod_grupo": "03", "calificacion": 3.4},
    {"cod_grupo": "02", "calificacion": 2.5},
    {"cod_grupo": "01", "calificacion": 3.2},
    {"cod_grupo": "03", "calificacion": 4.7},
    {"cod_grupo": "02", "calificacion": 4.2},
    {"cod_grupo": "01", "calificacion": 2.7},
    {"cod_grupo": "03", "calificacion": 4.1},
    {"cod_grupo": "02", "calificacion": 4},
    {"cod_grupo": "01", "calificacion": 3.8},
]


def promedio_notas(datos: list) -> dict:
    total_alumnos = 0
    nota_total = 0
    nota_g_a = 0
    nota_g_b = 0
    nota_g_c = 0
    total_alum_a = 0
    total_alum_b = 0
    total_alum_c = 0
    promedio_g_a = 0
    promedio_g_b = 0
    promedio_g_c = 0
    promedio_total = 0

    for notas in datos:
        total_alumnos += 1
        nota_total += notas["calificacion"]
        promedio_total = round((nota_total / total_alumnos), 2)
        if notas["cod_grupo"] == "01":
            nota_g_a += notas["calificacion"]
            total_alum_a += 1
            promedio_g_a = round((nota_g_a / total_alum_a), 2)
        elif notas["cod_grupo"] == "02":
            nota_g_b += notas["calificacion"]
            total_alum_b += 1
            promedio_g_b = round((nota_g_a / total_alum_b), 2)
        elif notas["cod_grupo"] == "03":
            nota_g_c += notas["calificacion"]
            total_alum_c += 1
            promedio_g_c = round((nota_g_c / total_alum_c), 2)

    print("\n")
    resultado = {
        "promedio_calificaciones_programa": promedio_total,
        "promedio_calificaciones_grupo_01": promedio_g_a,
        "promedio_calificaciones_grupo_02": promedio_g_b,
        "promedio_calificaciones_grupo_03": promedio_g_c,
        "numero_de_alumnos_grupo_01": total_alum_a,
        "numero_de_alumnos_grupo_02": total_alum_b,
        "numero_de_alumnos_grupo_03": total_alum_c,
        "Total_alumnos_matriculados_en_matematicas_I": total_alumnos,
    }

    return resultado


print(promedio_notas(datos))
print("\n")
