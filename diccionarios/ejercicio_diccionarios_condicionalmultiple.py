'''
Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un porcentaje de su salario mensual que depende de su 
antigüedad en la empresa de acuerdo con la siguiente

Tiempo
menosde 1 año                   5% del salario
1 año o más y menos de 2 años   7% del salario
2 años y menos de 5 años        10% del salario
5 años y menos de 10 años       15% del salario
10 años o mas                   20% del salario
'''

def asignacion_incremento(reporte: dict) -> dict:
    return (reporte ['nombre']+" - "+ "Salario: "+ str(reporte['salario'])+ " " + "Antiguedad " + str(reporte['antiguedad']) + " " + "años" + " " + reporte['valor_incremento'])


def definir_aumento(diccionario: dict) -> dict:
    if(diccionario['antiguedad']< 1):
        aumento= "El incremento salarial es del 5 por ciento"
    elif(diccionario['antiguedad']>=1 and diccionario['antiguedad'] <= 2):
        aumento ="El incremento salarial es del 7 por ciento"
    elif(diccionario['antiguedad']>=5 and diccionario['antiguedad'] <= 10):
        aumento ="El incremento salarial es del 15 por ciento"
    else:
        aumento ="El incremento salarial es del 20 por ciento"
    
    diccionario_respuesta = {
        "nombre" : diccionario['nombre'],
        "salario": diccionario['salario'],
        "antiguedad" : diccionario['antiguedad'],
        "valor_incremento": aumento
    }

    return diccionario_respuesta
print('\n')



diccionario = {
    'nombre': "Carolina Reyes",
    'salario': 50000000.0,
    'antiguedad': 10
    }
    
print(asignacion_incremento(definir_aumento(diccionario)))
print('\n')