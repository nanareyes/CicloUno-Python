"""
correo = input("Ingresar correo: ")
numArrobas = 0
"""
"""
for i in range(len(correo)):
    if correo[i] == "@":
        numArrobas += 1
elementosCorreo = list()
diccionarioCorreo = dict()
if numArrobas == 1:
    print("correo válido")
    elementosCorreo = correo.split("@")
    diccionarioCorreo["Nombre Usuario"] = elementosCorreo[0]
    diccionarioCorreo["Dominio"] = elementosCorreo[1]
    print("Nombre de usuario", elementosCorreo[0])
    print("Segunda Posición", elementosCorreo[1])
else:
    print("correo inválido")
# guardar la inf en pantalla y mostrarla en pantalla
print("Nombre de usuario: ", diccionarioCorreo["Nombre Usuario"])
print("Dominio: ", diccionarioCorreo["Dominio"])
"""

"""
for i in range(len(correo)):
    if correo[i] == "@":
        numArrobas += 1
elementosCorreo = list()
diccionarioCorreo = dict()
if numArrobas == 1:
    print("correo válido")
    elementosCorreo = correo.split("@")
    diccionarioCorreo = {
        "Nombre Usuario": elementosCorreo[0],
        "Dominio": elementosCorreo[1],
    }
else:
    print("correo inválido")
# guardar la inf en pantalla y mostrarla en pantalla
print("Accediendo a cada posición: ")
print("Nombre de usuario: ", diccionarioCorreo["Nombre Usuario"])
print("Dominio: ", diccionarioCorreo["Dominio"])
"""

# Solicitar varios correos y almacenar en una lista de diccionarios aquellos que son válidos


def correoValido(correo):
    numArrobas = 0

    for i in range(len(correo)):
        if correo[i] == "@":
            numArrobas += 1
    if numArrobas == 1:
        return True
    else:
        return False


# Solicitar 3 correos y clasificarlos -> guardarlos en una lista de diccionarios
listaCorreosValidos = list()
for _ in range(3):
    # Solicitar correo al usuario
    correo = input("Ingresar correo: ")
    elementosCorreo = list()
    diccionarioCorreo = dict()
    if correoValido(correo):
        elementosCorreo = correo.split("@")
        diccionarioCorreo = {
            "Nombre Usuario": elementosCorreo[0],
            "Dominio": elementosCorreo[1],
        }
        listaCorreosValidos.append(diccionarioCorreo)
    else:
        print("Correo inválido")

# Mostrar contenedor final (colección de correos válidos)
listaCorreosValidos = tuple(listaCorreosValidos)
print(listaCorreosValidos)
