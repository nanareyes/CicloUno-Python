def poblacion(poblacion):

    '''
    Función que regresa la persona cuya edad es mayor, dentro de una población de 4 personas

    ​-La función recibe un diccionario como parametro que contiene la población y cuyas llaves son
    'nombre1', 'edad1', 'nombre2', 'edad2', 'nombre3', 'edad3', 'nombre4', 'edad4',


    ​-En caso de que existan edades iguales regresar la primera persona de la población con la edad igual

    Parámetros:
    -----------
        poblacion (dict):
            ​datos (nombre y edad) de la población (4 personas)

    Retorna: -
    -------
        str:
        -En caso de éxito, retorna una cadena de caracteres de la forma.
    ​       "Con {edad} años, el mayor de todos es: {nombre}."

        -En caso de que el parametro no sea un diccionario "
            Error en los datos recibidos." """'''

    "datos de prueba"
    # {'nombre1':'Juan', 'edad1':25, 'nombre2':'Maria', 'edad2':34, 'nombre3':'Camila', 'edad3':19, 'nombre4':'Carlos', 'edad4':33 }

    # ​{'nombre1':'Juan', 'edad1':35, 'nombre2':'Maria', 'edad2':24, 'nombre3':'Camila', 'edad3':19, 'nombre4':'Carlos', 'edad4':45 }

    try:
        poblacion["edad1"]
    except:
        return "Error en los datos recibidos."

    if (
        poblacion["edad1"] >= poblacion["edad2"]
        and poblacion["edad1"] >= poblacion["edad3"]
        and poblacion["edad1"] >= poblacion["edad4"]
    ):

        return f"Con {poblacion['edad1']} años, el mayor de todos es: {poblacion['nombre1']}."
    elif (
        poblacion["edad2"] >= poblacion["edad3"]
        and poblacion["edad2"] >= poblacion["edad4"]
    ):
        return f"Con {poblacion['edad2']} años, el mayor de todos es: {poblacion['nombre2']}."
    elif poblacion["edad3"] >= poblacion["edad4"]:
        return f"Con {poblacion['edad3']} años, el mayor de todos es: {poblacion['nombre3']}."
    else:
        return f"Con {poblacion['edad4']} años, el mayor de todos es: {poblacion['nombre4']}."


print(
    poblacion(
        {
            "nombre1": "Juan",
            "edad1": 25,
            "nombre2": "Maria",
            "edad2": 34,
            "nombre3": "Camila",
            "edad3": 19,
            "nombre4": "Carlos",
            "edad4": 33,
        }
    )
)

print(
    poblacion(
        {
            "nombre1": "Juan",
            "edad1": 35,
            "nombre2": "Maria",
            "edad2": 24,
            "nombre3": "Camila",
            "edad3": 19,
            "nombre4": "Carlos",
            "edad4": 45,
        }
    )
)
