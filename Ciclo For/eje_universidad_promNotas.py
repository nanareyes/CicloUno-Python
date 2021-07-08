"""
En una universidad se desea conocer el promedio de calificaciones de la asignatura Matemática I de la carrera de Ingeniería Civil, el programa cuenta con tres grupos, se necesita calcular el promedio de calificaciones del primer parcial por cada grupo y el promedio de calificaciones a nivel general, por otra parte, se necesita conocer el número de alumnos de cada grupo y el total general.
Se debe procesar n cantidad de datos de los estudiantes con la siguiente información:
1. Código grupo
2. Calificación 
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
Código_grupo: Puede ser 01, 02 y 03
calificacion: int
Ejemplo Datos
datos: list = [
    {
        "cod_grupo": "01",
        "calificacion": 5
    },
    {
        "cod_grupo": "02",
        "calificacion": 2
    },
    {
        "cod_grupo": "01",
        "calificacion": 3
    },
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


def promedio_calificaciones(datos: list) -> dict:
    Total_calificaciones = 0
    Total_calificaciones_grupo1 = 0
    Total_calificaciones_grupo2 = 0
    Total_calificaciones_grupo3 = 0
    Promedio_calificaciones_grupo1 = 0
    Promedio_calificaciones_grupo2 = 0
    Promedio_calificaciones_grupo3 = 0
    Promedio_calificaciones_total = 0
    Total_alumnos = 0
    Alumnos_grupo1 = 0
    Alumnos_grupo2 = 0
    Alumnos_grupo3 = 0
    for item in datos:
        Total_calificaciones += item["calificacion"]
        Total_alumnos += 1
        Promedio_calificaciones_total = round((Total_calificaciones / Total_alumnos), 2)
        if item["cod_grupo"] == "01":
            Total_calificaciones_grupo1 += item["calificacion"]
            Alumnos_grupo1 += 1
            Promedio_calificaciones_grupo1 = round(
                (Total_calificaciones_grupo1 / Alumnos_grupo1), 2
            )
        elif item["cod_grupo"] == "02":
            Total_calificaciones_grupo2 += item["calificacion"]
            Alumnos_grupo2 += 1
            Promedio_calificaciones_grupo2 = round(
                (Total_calificaciones_grupo2 / Alumnos_grupo2), 2
            )
        elif item["cod_grupo"] == "03":
            Total_calificaciones_grupo3 += item["calificacion"]
            Alumnos_grupo3 += 1
            Promedio_calificaciones_grupo3 = round(
                (Total_calificaciones_grupo3 / Alumnos_grupo3), 2
            )
    resultado: dict = {
        "Promedio_calificaciones_del_programa": Promedio_calificaciones_total,
        "Promedio_calificaciones_grupo_01": Promedio_calificaciones_grupo1,
        "Promedio_calificaciones_grupo_02": Promedio_calificaciones_grupo2,
        "Promedio_calificaciones_grupo_03": Promedio_calificaciones_grupo3,
        "Alumnos_matriculados_matemáticas_01": Total_alumnos,
        "Alumnos_grupo_01": Alumnos_grupo1,
        "Alumnos_grupo_02": Alumnos_grupo2,
        "Alumnos_grupo_03": Alumnos_grupo3,
    }
    return resultado


datos: list = [
    {"cod_grupo": "01", "calificacion": 5},
    {"cod_grupo": "02", "calificacion": 2},
    {"cod_grupo": "01", "calificacion": 3},
    {"cod_grupo": "03", "calificacion": 4},
]
print(promedio_calificaciones(datos))
