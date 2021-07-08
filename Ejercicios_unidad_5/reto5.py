import numpy as np
import pandas as pd
import os

url = "https://raw.githubusercontent.com/pepija/mintic-p66/main/examen_colesterol.csv"


def examen(ruta_archivo_csv: str) -> dict:
    if ruta_archivo_csv.endswith(".csv"):
        try:
            current_dir = os.path.dirname(os.path.realpath(__file__))
            url = os.path.join(current_dir, ruta_archivo_csv)
            df_examen = pd.read_csv(
                "https://raw.githubusercontent.com/pepija/mintic-p66/main/examen_colesterol.csv"
            )
        except:
            return "No es posible leer los Datos, verique la ruta."
        df_examen.groupby("sexo").agg(np.mean)
        print(df_examen.groupby("sexo").agg(np.mean))
        print("\n")
    else:
        return "Extensión Errónea"

    DF = df_examen.to_dict()

    return DF
