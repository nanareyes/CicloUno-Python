""" 
Un centro hospitalario requiere realizar un análisis de los resultados de exámenes de Triglicéridos realizados en el mes  
de mayo. Se desea conocer el promedio de las edades, peso, altura y resultado del examen, se debe agrupar por sexo, de  
tal manera que se pueda conocer la correlación que existe entre las variables y el resultado del examen de laboratorio. 

os datos están almacenados en el archivo examen_trigliceridos.csv disponible en el repositorio de Github. Escriba una función que  
reciba como parámetro el nombre del archivo, incluyendo la extensión y lo lea desde el directorio actual. Con los datos contenidos en  
este archivo, construir un dataFrame con el método groupby y el módulo Numpy, utilizando la función .mean para hallar los promedios  
necesarios. 
 
Utilice el método df.to_dict() para retornar un diccionario con la información solicitada. 
"""
import numpy as np
import pandas as pd
import os


def examen(ruta_archivo_csv: str) -> dict:
    # Validar apertura del archivo
    if ruta_archivo_csv.endswith(".csv"):
        try:
            # Creamos un dataframe a partir del fichero csv
            current_dir = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(current_dir, ruta_archivo_csv)
            df_examen = pd.read_csv(filename)
        except:
            return "No es posible leer los Datos, verique la ruta."
        # seleccionamos solo los elementos que se necesitan
        # por el nombre corespondiente.
        df_examen.groupby("sexo").agg(np.mean)
        print(df_examen.groupby("sexo").agg(np.mean))
        print("\n")
    else:
        return "Extensión Errónea"

    # Preparar Salida
    DF = df_examen.to_dict()

    return DF


print(examen("examen_trigliceridos.csv"))
