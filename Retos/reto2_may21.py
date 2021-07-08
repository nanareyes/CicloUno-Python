"""
En una universidad se desea conocer el promedio de calificaciones de la asignatura Matemática I de la carrera de Ingeniería Civil,
el programa cuenta con tres grupos, se necesita calcular el promedio de calificaciones del primer parcial por cada grupo y el promedio 
de calificaciones a nivel general, por otra parte, se necesita conocer el número de alumnos de cada grupo y el total general.

Se debe procesar n cantidad de datos de los estudiantes con la siguiente información:
1.  Código grupo
2.  Calificación 

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


datos: list = [
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
    {"cod_progrma": "01", "valor_inscripcion": 120000},
    {"cod_progrma": "02", "valor_inscripcion": 150000},
    {"cod_progrma": "03", "valor_inscripcion": 110000},
]


def registro(datos: list) -> dict:
    total_inscritos_licenciatura = 0
    total_inscritos_electronica = 0
    total_inscritos_sistemas = 0
    total_recaudo_licenciatura = 0
    total_recaudo_electronica = 0
    total_recaudo_sistemas = 0
    total = 0

    for inscritos in datos:
        if inscritos["cod_progrma"] == "03":
            total_recaudo_licenciatura += inscritos["valor_inscripcion"]
            total_inscritos_licenciatura += 1
        elif inscritos["cod_progrma"] == "01":
            total_recaudo_electronica += inscritos["valor_inscripcion"]
            total_inscritos_electronica += 1
        else:
            total_recaudo_sistemas += inscritos["valor_inscripcion"]
            total_inscritos_sistemas += 1
        total = inscritos["valor_inscripcion"] + total
    print("\n")
    resultado = {
        "total_licenciatura": total_inscritos_licenciatura,
        "total_electronica": total_inscritos_electronica,
        "total_sistemas ": total_inscritos_sistemas,
        "recaudo_licenciatura": total_recaudo_licenciatura,
        "recaudo_electronica": total_recaudo_electronica,
        "recaudo_sistemas": total_recaudo_sistemas,
        "total_recaudo": total,
    }
    return resultado


print(registro(datos))
print("\n")
