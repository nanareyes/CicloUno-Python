"""
Una EPS desea conocer el numero personas atendidas en su programa de vacunación contra el COVID 19, la información debe ir discriminada de la siguiente manera: 
Número total de personas atendidas, 
número total de mujeres atendidas, 
número total de hombres atendidos, 
personas atendidas entre los rangos de edades de 40 a 49, 50 a 59, 60 a 69, 70 a 79 y mayores de 80.
La ciudad cuenta con 8 comunas, se desea conocer también el número de personas atendidas por comuna y las personas que en los últimos 3 meses tuvieron COVID 19.

Se debe procesar n cantidad de datos de personas con la siguiente información:
1. Edad
2. Sexo
3. Comuna
4. Covid_antes_SN

    Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
    1. Edad: int
    2. Sexo: f/m
    3. Comuna: Puede ser de la 01 a la 08
    4. Covid_antes: puede ser afirmativo o negativo (s/n)

    Ejemplo Datos
    datos: list = [
        {
            "edad": 40
            "sexo": f
            "comuna": 04
            "covid_antes": n
        },
    ]
La respuesta debe retornar un diccionario con la siguiente información:
# total de personas atendidas
# total de mujeres atendidas
# total de hombres atendidos
# total de personas atendidas con edades entre los 40 y 49 años.
# total de personas atendidas con edades entre los 50 y 59 años.
# total de personas atendidas con edades entre los 60 y 69 años.
# total de personas atendidas con edades entre los 70 y 79 años.
# total de personas atendidas mayores de 80 años.
"""
import pprint

datos: list = [
    {"edad": 60, "sexo": "f", "comuna": "04", "covid_antes": "n"},
    {"edad": 73, "sexo": "m", "comuna": "05", "covid_antes": "n"},
    {"edad": 40, "sexo": "m", "comuna": "03", "covid_antes": "n"},
    {"edad": 66, "sexo": "m", "comuna": "02", "covid_antes": "n"},
    {"edad": 40, "sexo": "m", "comuna": "04", "covid_antes": "n"},
    {"edad": 68, "sexo": "m", "comuna": "03", "covid_antes": "s"},
    {"edad": 73, "sexo": "m", "comuna": "04", "covid_antes": "s"},
    {"edad": 50, "sexo": "m", "comuna": "04", "covid_antes": "n"},
    {"edad": 49, "sexo": "f", "comuna": "04", "covid_antes": "n"},
    {"edad": 69, "sexo": "f", "comuna": "04", "covid_antes": "n"},
]


def vacunados(datos: list) -> dict:
    total_personas_atendidas = 0
    total_mujeres_atendidas = 0
    total_hombres_atendidos = 0
    total_atendidas_hasta_49 = 0
    total_atendidas_hasta_59 = 0
    total_atendidas_hasta_69 = 0
    total_atendidas_hasta_79 = 0
    total_atendidas_mayores_de80 = 0
    total_comuna1 = 0
    total_comuna2 = 0
    total_comuna3 = 0
    total_comuna4 = 0
    total_comuna5 = 0
    total_comuna6 = 0
    total_comuna7 = 0
    total_comuna8 = 0
    total_personas_covid = 0

    for atendidos in datos:
        total_personas_atendidas += 1
        if atendidos["sexo"] == "f":
            total_mujeres_atendidas += 1
        else:
            total_hombres_atendidos += 1
        if atendidos["edad"] >= 40 and atendidos["edad"] <= 49:
            total_atendidas_hasta_49 += 1
        elif atendidos["edad"] >= 50 and atendidos["edad"] <= 59:
            total_atendidas_hasta_59 += 1
        elif atendidos["edad"] >= 60 and atendidos["edad"] <= 69:
            total_atendidas_hasta_69 += 1
        elif atendidos["edad"] >= 70 and atendidos["edad"] <= 79:
            total_atendidas_hasta_79 += 1
        else:
            total_atendidas_mayores_de80 += 1
        if atendidos["comuna"] == "01":
            total_comuna1 += 1
        elif atendidos["comuna"] == "02":
            total_comuna2 += 1
        elif atendidos["comuna"] == "03":
            total_comuna3 += 1
        elif atendidos["comuna"] == "04":
            total_comuna4 += 1
        elif atendidos["comuna"] == "05":
            total_comuna5 += 1
        elif atendidos["comuna"] == "06":
            total_comuna6 += 1
        elif atendidos["comuna"] == "07":
            total_comuna7 += 1
        elif atendidos["comuna"] == "08":
            total_comuna8 += 1
        elif atendidos["covid_antes"] == "s":
            total_personas_covid += 1

    print("\n")

    resultado = {
        "total de personas atendidas": total_personas_atendidas,
        "total de mujeres atendidas": total_mujeres_atendidas,
        "total de hombres atendidos": total_hombres_atendidos,
        "total de personas atendidas con edades entre los 40 y 49 años": total_atendidas_hasta_49,
        "total de personas atendidas con edades entre los 50 y 59 años": total_atendidas_hasta_59,
        "total de personas atendidas con edades entre los 60 y 69 años": total_atendidas_hasta_69,
        "total de personas atendidas con edades entre los 70 y 79 años": total_atendidas_hasta_79,
        "total de personas atendidas mayores de 80 años": total_atendidas_mayores_de80,
        "total personas comuna 01": total_comuna1,
        "total personas comuna 02": total_comuna2,
        "total personas comuna 03": total_comuna3,
        "total personas comuna 04": total_comuna4,
        "total personas comuna 05": total_comuna5,
        "total personas comuna 06": total_comuna6,
        "total personas comuna 07": total_comuna7,
        "total personas comuna 08": total_comuna8,
        "total personas con covid": total_personas_covid,
    }
    return resultado


pprint.pprint(vacunados(datos))
print("\n")
