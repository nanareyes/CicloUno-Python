# Requerimiento -> Determinar si un correo tiene le número de arrobas adecuado (1)

# Solicitar correo al usuario
correo = input("Ingresar correo: ")
numArrobas = 0

for caracter in correo:
    if caracter == "@":
        numArrobas += 1
if caracter == 1:
    print("correo válido")
else:
    print("correo inválido")

# o utilizando el for y el len para hacer un recorrido por los carácteres
for i in range(len(correo)):
    if correo[i] == "@":
        numArrobas += 1
if numArrobas == 1:
    print("correo válido")
else:
    print("correo inválido")

# Obtener el usuario y el dominio si es válido (2)
for i in range(len(correo)):
    if correo[i] == "@":
        numArrobas += 1
elementosCorreo = list()
if numArrobas == 1:
    print("correo válido")
    elementosCorreo = correo.split(
        "@"
    )  # Split es un método de las cadenas para devolver listas
    print("Nombre de usuario", elementosCorreo[0])
    print("Segunda Posición", elementosCorreo[1])
else:
    print("correo inválido")

# (3) Solicitar varios correos y almacenar en una lista de diccionarios aquellos que son válidos


def correoValido(correo):
    numArrobas = 0
    # for caracter in correo:
    #     if caracter == '@':
    #         numArrobas += 1
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
        # print('Correo válido')
        elementosCorreo = correo.split("@")
        # Alternativa de actualización de diccionario
        # diccionarioCorreo['Nombre Usuario'] = elementosCorreo[0]
        # diccionarioCorreo['Dominio'] = elementosCorreo[1]
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

# Recorrido contenedor de contenedores
for i, correo in enumerate(listaCorreosValidos):
    print("---------------------------")
    print(f"Correo Válido No. {i+1}")
    for llave, valor in correo.items():
        print(f"{llave}: {valor}")
