# se van a asignar unas becas, que dependen del estrato social y el promedio de notas

# PARA ARREGLAR 

def asignacion_becas(dicReporte: dict) -> dict:
    return dicReporte['estudiante']+" - "+"Tipo Beca: "(dicReporte['tipoBeca'])

# Funcion para definir el tipo de beca

def definir_beca(datos_estudiante: dict) -> dict:
    if(datos_estudiante['promedio'] >= 3.5) and (datos_estudiante['estrato']<=2):
        beca = "La beca incluye el sostenimiento económico y el pago del 100 por ciento de los costos académicos"
    elif (datos_estudiante['promedio'] == 3.5) and (datos_estudiante['estrato'] ==3):
        beca = "La beca incluye el sostenimiento económico y el pago del 40 por ciento de los costos académicos"
    elif (datos_estudiante['promedio'] >= 4.0) and (datos_estudiante['estrato'] ==3):
        beca = "La beca incluye el sostenimiento económico y el pago del 70 por ciento de los costos académicos"
    elif (datos_estudiante['promedio'] >= 4.0) and (datos_estudiante['estrato'] ==4):
        beca = "La beca incluye el sostenimiento económico y el pago del 30 por ciento de los costos académicos"
    else:
        beca = "No se otroga la beca"

    diccionario_respuesta = {
        "Estudiante" : datos_estudiante['Estudiante'],
        "tipoBeca": beca
    }

    return diccionario_respuesta
print('\n')

# Datos de prueba
datos_estudiante = {
    "id_estudiante": "t001",
    "estudiante": "Diana Reyes",
    "promedio": 3.5,
    "estrato": 2
}

print(asignacion_becas(definir_beca(datos_estudiante)))