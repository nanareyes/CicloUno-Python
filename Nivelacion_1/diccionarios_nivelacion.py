# Los diccionarios son contenedores de datos
# Y lso elemntos internos están asignados a una llave valor y se pueden separar con comas 

# Sintaxis
'''
diccionario1 = {
    'nombre': 'Carolina',
    'apellido': 'Reyes',
    'celular': 3207483074,
    34: 'código'
}
print (type(diccionario1))
print (diccionario1['apellido'])
'''

def notas(dicnotas):
    promedio = round((dicnotas['nota1'] + dicnotas['nota2'] + dicnotas['nota3'])/3,2) 
    maximo = max(dicnotas['nota1'], dicnotas['nota2'], dicnotas['nota3'])
    minimo = min(dicnotas['nota1'], dicnotas['nota2'], dicnotas['nota3'])
    if promedio >= 0 and promedio < 3:  # La condición se expresa con variables y operadores ( y siempre debo tener presente lo que voy a comparar)
        rendimiento = 'Bajo'
    elif promedio >= 3 and  promedio < 4:
        rendimiento = 'Medio'
    elif promedio >= 4 and promedio <= 5:
        rendimiento = 'Alto'
    

    return  f'El estudiante tiene una nota promedio de {promedio}, su mayor nota fue {maximo},  su menor nota fue {minimo}, y su rendimiento fue {rendimiento}' 

dicnotas = {
    'nota1': 3.5,
    'nota2': 4,
    'nota3': 4.6

}
print(notas(dicnotas)) # con el print llamo el diccionario de notas

