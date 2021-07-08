print("\n")


def cantidad_inscritos(datos: list) -> dict:
    numero_inscritos_01 = 0
    valor_recaudo_01 = 0
    numero_inscritos_02 = 0
    valor_recaudo_02 = 0
    numero_inscritos_03 = 0
    valor_recaudo_03 = 0
    for estudiante in datos:
        if estudiante["cod_programa"] == "01":
            numero_inscritos_01 += 1
            valor_recaudo_01 += estudiante["valor_inscripcion"]
        elif estudiante["cod_programa"] == "02":
            numero_inscritos_02 += 1
            valor_recaudo_02 += estudiante["valor_inscripcion"]
        elif estudiante["cod_programa"] == "03":
            numero_inscritos_03 += 1
            valor_recaudo_03 += estudiante["valor_inscripcion"]
    resultado: dict = {
        "Total Inscritos licenciatura matematicas": numero_inscritos_01,
        "Total Recaudo licenciatura matematicas": valor_recaudo_01,
        "Total Inscritos Tecnologia en electronica": numero_inscritos_02,
        "Total Recaudo Tecnologia en electronica": valor_recaudo_02,
        "Total Inscritos Tecnologia de sistemas": numero_inscritos_03,
        "Total Recaudo Tecnologia en electroinica": valor_recaudo_03,
    }
    return resultado


datos: list = [
    {"cod_programa": "01", "valor_inscripcion": 600000},
    {"cod_programa": "02", "valor_inscripcion": 800000},
    {"cod_programa": "03", "valor_inscripcion": 400000},
    {"cod_programa": "03", "valor_inscripcion": 600000},
    {"cod_programa": "02", "valor_inscripcion": 1000000},
    {"cod_programa": "01", "valor_inscripcion": 400000},
    {"cod_programa": "02", "valor_inscripcion": 700000},
]
print(cantidad_inscritos(datos))
print("\n")
