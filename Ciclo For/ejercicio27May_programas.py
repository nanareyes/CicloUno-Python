"""

En una Universidad existen tres programas académicos, que son: Licenciatura Matemáticas, Tecnología en Electrónica y Tecnología de Sistemas, los cuales tienen 
un costo de inscripción de $120.000 para Tecnología Electrónica, $150.000 para Matemáticas y $110.000 para Tecnología de Sistemas,
Se desea conocer el numero de inscritos en cada programa y el total recaudado por concepto de inscripción en cada programa.
Se debe procesar n cantidad de inscritos con la siguiente información:
1. Código del programa
2. Valor Inscripción

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
1. cod_programa: “01 - Licenciatura Matemáticas” o “02 - Tecnología en Electrónica” o “03 - Tecnología de Sistemas”
2. valor_inscripcion: int

EJEMPLO diccionario
datos: list = [
    {
        "cod_progrma": "01",
        "valor_inscripcion": 120000
    },
    {
        "cod_progrma": "02",
        "valor_inscripcion": 150000
    },
{
        "cod_progrma": "03",
        "valor_inscripcion": 110000
    },
    
]

La respuesta debe retornar un diccionario con la siguiente información:

1. Total inscriptos por programa
2. Recaudo_total por programa

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
