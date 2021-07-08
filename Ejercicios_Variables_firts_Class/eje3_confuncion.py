'''
Elaborar un algoritmo que permita averiguar si una persona debe sacar cédula de ciudadanía, si la persona 
es mayor de 17 años debe imprimir "Debe sacar cédula de ciudadanía" en caso contratrio imprimir
"No debe solicitar cédula"

'''

def cedula_edad(e):
    if e <= 17:
        print("No debe solicitar cédula")
    else:
        e > 17
        print ("Debe sacar cédula de ciudadanía")

cedula = int(input("Digite la edad: "))
funcion = cedula_edad(cedula)

print('\n')
print(funcion)

