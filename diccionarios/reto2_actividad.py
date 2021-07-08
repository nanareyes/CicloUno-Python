def prestamo(informacion: dict) -> dict:

    id_prestamo = informacion["id_prestamo"]
    casado = informacion["casado"]
    dependientes = informacion["dependientes"]
    educacion = informacion.get("educacion")
    independiente = informacion["independiente"]
    i_d = informacion["i_d"]
    i_c = informacion["i_c"]
    c_p = informacion["c_p"]
    p_p = informacion["p_p"]
    historia_credito = informacion["historia_credito"]
    tipo_propiedad = informacion["tipo_propiedad"]

    if historia_credito == 1:
        if i_c > 0 and (i_d / 9) > c_p:
            return {"id_prestamo": id_prestamo, "aprobado": True}
        else:
            if dependientes > 2 and independiente == "Si":
                if (i_c / 12) > c_p:
                    return {"id_prestamo": id_prestamo, "aprobado": True}
            elif c_p < 200:
                return {"id_prestamo": id_prestamo, "aprobado": True}
    else:
        if independiente == "Si":
            if not (casado == "Si" and dependientes > 1):
                if (i_d / 10) > c_p or (i_c / 10) > c_p:
                    if c_p < 180:
                        return {"id_prestamo": id_prestamo, "aprobado": True}
                else:
                    return {"id_prestamo": id_prestamo, "aprobado": False}
            else:
                return {"id_prestamo": id_prestamo, "aprobado": False}
        # independiente == "No"
        else:
            if not tipo_propiedad == "Semiurbano" and dependientes < 2:
                if educacion == "Graduado":
                    if (i_d / 11) > c_p and (i_c / 11) > c_p:
                        return {"id_prestamo": id_prestamo, "aprobado": True}
                else:
                    return {"id_prestamo": id_prestamo, "aprobado": False}
            else:
                return {"id_prestamo": id_prestamo, "aprobado": False}

    return {"id_prestamo": id_prestamo, "aprobado": False}


"""
diccionario = {
    'id_prestamo': "001c",
    'casado': 'No',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'Si',
    'i_d': 4692,
    'i_c': 0,
    'c_p': 106,
    'p_p': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
    }


diccionario = {
    'id_prestamo': "002c",
    'casado': 'No',
    'dependientes': 3,
    'educacion': 'No Graduado',
    'independiente': 'No',
    'i_d': 1830,
    'i_c': 0,
    'c_p': 100,
    'p_p': 360,
    'historia_credito': 0,
    'tipo_propiedad': 'Urbano'
    }

"""
diccionario = {
    "id_prestamo": "003c",
    "casado": "No",
    "dependientes": 0,
    "educacion": "No Graduado",
    "independiente": "No",
    "i_d": 3748,
    "i_c": 1668,
    "c_p": 110,
    "p_p": 360,
    "historia_credito": 1,
    "tipo_propiedad": "Semiurbano",
}

print(prestamo(diccionario))
