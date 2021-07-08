'''
Pida al usuario la edad y el sexo, para que la computadora le indique si ya puede jubilarse. 
Tome en cuenta que un Hombre se puede jubilar cuando tenga 62 años o más, en cambio, una mujer mayor se jubilara si tiene más de 57 años.
'''

def pension(e, s):
    if (e >= 57):
        if (s == "femenino"):
            return "Ya puede jubilarse"
        else:
            if (e >= 62):
                return "Ya puede jubilarse"
            else:
                return "No puede jubilarse aún"
    else:
        return "No puede jubilarse aún"


edad = int(input("Digite su edad: "))
sexo = input("Digite sexo: ")
jubilacion = pension(edad, sexo)
print(jubilacion)




