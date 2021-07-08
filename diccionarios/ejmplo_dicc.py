# Pasar informacion a través de diccionarios

'''
Los diccionarios ofrecen la posibilidad de empaquetar o encapsular varias variables para facilitar el envio de parámetros.
'''
# Encapsulamiento con Diccionario
# Ejemplo

def promedioNotas(dicNotas): # dicNotas en un Diccionario que
    sumatoria = 0 # Inicializo la variable sumatoria
    sumatoria += dicNotas['nota1']  #+= es un operador que va sumando los valores que va agregando
    sumatoria += dicNotas['nota2']
    sumatoria += dicNotas['nota3']
    promedio = round(sumatoria/3,2) # El 2 hace referencia a la cantidad de decimales 
    return promedio

# creo el diccionario dicNotas ={}
dicNotas = {
    "nota1": 2.5,
    "nota2": 3.5,
    "nota3": 4.5
}

print("El promedio es: ", promedioNotas(dicNotas))

diccionario = {
    'nombre' : 'Diana',
    'apellido': 'Reyes',
    'edad': '39',
    'dinero': 50000
}

print(diccionario.get('dinero'))
