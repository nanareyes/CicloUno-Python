def EPS_COVID(datos: list) -> dict:
    Total_atendidos = 0
    Mujeres: str = "f"
    Hombres: str = "m"
    Total_mujeres = 0
    Total_hombres = 0
    Total_cuarenta_cuarentaynueve = 0
    Total_cincuenta_cincuentaynueve = 0
    Total_sesenta_sesentaynueve = 0
    Total_sententa_setentaynueve = 0
    Total_mayores_ochenta = 0
    for item in datos:
        Total_atendidos += 1
        if item["sexo"] == Mujeres:
            Total_mujeres += 1
        elif item["sexo"] == Hombres:
            Total_hombres += 1
        if item["edad"] >= 40 and item["edad"] < 50:
            Total_cuarenta_cuarentaynueve += 1
        elif item["edad"] >= 50 and item["edad"] < 60:
            Total_cincuenta_cincuentaynueve += 1
        elif item["edad"] >= 60 and item["edad"] < 70:
            Total_sesenta_sesentaynueve += 1
        elif item["edad"] >= 70 and item["edad"] < 80:
            Total_sententa_setentaynueve += 1
        elif item["edad"] >= 80:
            Total_mayores_ochenta += 1
    resultado: dict = {
        "Total_personas_atendidas": Total_atendidos,
        "Total_mujeres_atendidas": Total_mujeres,
        "Total_hombres_atendidos": Total_hombres,
        "Total-de_personas_atendidas_con_edades_entre_los_40_y_49_años": Total_cuarenta_cuarentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_50_y_59_años": Total_cincuenta_cincuentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_60_y_69_años": Total_sententa_setentaynueve,
        "Total-de_personas_atendidas_con_edades_entre_los_70_y_79_años": Total_sesenta_sesentaynueve,
        "Total-de_personas_atendidas_mayores_80": Total_mayores_ochenta,
    }
    return resultado


import pprint

datos: list = [
    {"sexo": "f", "edad": 40, "comuna": "04", "covid_antes": "n"},
    {"sexo": "f", "edad": 49, "comuna": "05", "covid_antes": "n"},
    {"sexo": "m", "edad": 51, "comuna": "06", "covid_antes": "s"},
    {"sexo": "f", "edad": 62, "comuna": "07", "covid_antes": "s"},
    {"sexo": "m", "edad": 80, "comuna": "04", "covid_antes": "n"},
    {"sexo": "m", "edad": 62, "comuna": "05", "covid_antes": "s"},
    {"sexo": "m", "edad": 72, "comuna": "06", "covid_antes": "n"},
]
pprint.pprint(EPS_COVID(datos))
