def reportarBonificacion(dicReporte: dict) -> str:
    return dicReporte["empleado"] + " - Bonificación: " + dicReporte["bonificacion"]


def generarReporteBonificacion(dicEmpleado: dict) -> str:
    if dicEmpleado["antiguedad"] < 1:
        bonificacion = (
            "Tiene una Bonificación equivalente al 5 por ciento de su salario mensual"
        )
    else:
        if dicEmpleado["antiguedad"] >= 1 and dicEmpleado["antiguedad"] < 2:
            bonificacion = "Tiene una Bonificación equivalente al 7 por ciento de su salario mensual"
        else:
            if dicEmpleado["antiguedad"] >= 2 and dicEmpleado["antiguedad"] < 5:
                bonificacion = "Tiene una Bonificación equivalente al 10 por ciento de su salario mensual"
            else:
                if dicEmpleado["antiguedad"] >= 5 and dicEmpleado["antiguedad"] < 10:
                    bonificacion = "Tiene una Bonificación equivalente al 16 por ciento de su salario mensual"
                else:
                    bonificacion = "Tiene una Bonificación equivalente al 20 por ciento de su salario mensual"
    reporteBonificacion = {
        "bonificacion": bonificacion,
        "empleado": dicEmpleado["empleado"],
    }
    return reporteBonificacion


dicEmpleado = {"id_empleado": "id_001", "empleado": "Sandra Peña", "antiguedad": 1}
dicEmpleado = {"id_empleado": "id_002", "empleado": "Pedro Lopez", "antiguedad": 4}

print(reportarBonificacion(generarReporteBonificacion(dicEmpleado)))
