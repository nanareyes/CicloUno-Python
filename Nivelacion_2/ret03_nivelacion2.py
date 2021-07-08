def poblacion(poblacion):

    """Función que regresa la persona cuya edad es mayor, dentro de una población de N personas

    ​    -La función recibe una lista de diccionarios como parametro que contiene la población, las llaves del diccionario son 'nombre', 'edad'
        -En caso de que existan edades iguales regresar la primera persona de la población con la edad igual


    ​Parámetros:
    -----------
        poblacion (dict):
            datos (nombre y edad) de la población (N personas)

    ​Retorna:
    --------
        str:
            -En caso de éxito, retorna una cadena de caracteres de la forma.
                "Con {edad} años, el mayor de todos es: {nombre}."

            ​-En caso de que el parametro no sea una lista con diccionarios
                "Error en los datos recibidos." """
    try:
        poblacion[0]["edad"]
    except:
        return "Error en los datos recibidos."

    edad_mayor = 0
    nombre_mayor = ""

    for persona in poblacion:
        if persona["edad"] > edad_mayor:
            edad_mayor = persona["edad"]
            nombre_mayor = persona["nombre"]
    return f"Con {edad_mayor} años, el mayor de todos es: {nombre_mayor}."


"""
datos_poblacion = [
    {"nombre": "Juan", "edad": 35},
    {"nombre": "Maria", "edad": 34},
    {"nombre": "Camila", "edad": 39},
]
"""


datos_poblacion = [
    {"nombre": "Felipe", "edad": 43},
    {"nombre": "Maria", "edad": 34},
    {"nombre": "Camila", "edad": 19},
    {"nombre": "Carlos", "edad": 33},
    {"nombre": "Juan", "edad": 43},
]
print(poblacion(datos_poblacion))
