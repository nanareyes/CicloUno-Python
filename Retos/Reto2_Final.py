"""

Tiempo
menosde 1 año                   5% del salario
1 año o más y menos de 2 años   7% del salario
2 años y menos de 5 años        10% del salario
5 años y menos de 10 años       15% del salario
10 años o mas                   20% del salario
"""


def reportarBonificacion(dicreporte: dict) -> str:
    return (
        dicreporte["empleado"] + "  " + "Bonificación: " + (dicreporte["bonificacion"])
    )


def generarReporteBonificacion(dicEmpleado: dict) -> str:
    if dicEmpleado["antiguedad"] < 1:
        bonificacion = (
            "Tiene una Bonificación equivalente al 6 por ciento de su salario mensual"
        )
    elif dicEmpleado["antiguedad"] >= 1 and dicEmpleado["antiguedad"] < 2:
        bonificacion = (
            "Tiene una Bonificación equivalente al 7 por ciento de su salario mensual"
        )
    elif (dicEmpleado["antiguedad"] >= 2) and (dicEmpleado["antiguedad"] < 5):
        bonificacion = (
            "Tiene una Bonificación equivalente al 10 por ciento de su salario mensual"
        )
    elif dicEmpleado["antiguedad"] >= 5 and dicEmpleado["antiguedad"] <= 10:
        bonificacion = (
            "Tiene una Bonificación equivalente al 16 por ciento de su salario mensual"
        )
    else:
        bonificacion = (
            "Tiene una bonificación equivalente al 20 por ciento de su salario mensual"
        )

    diccionario_respuesta = {
        "empleado": dicEmpleado["empleado"],
        "bonificacion": bonificacion,
    }

    return diccionario_respuesta


print("\n")


dicEmpleado = {"id_empleado": "id_001", "empleado": "Sandra Peña", "antiguedad": 1}
print(reportarBonificacion(generarReporteBonificacion(dicEmpleado)))
print("\n")
