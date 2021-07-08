'''
Elaborar un algoritmo que permita averiguar si una persona debe sacar cédula de ciudadanía, si la persona 
es mayor de 17 años debe imprimir "Debe sacar cédula de ciudadanía" en caso contratrio imprimir
"No debe solicitar cédula"

'''

edad = int(input("Digite su edad: "))

if edad > 17:
    print("Debe sacar cédula de ciudadanía")
else: 
    print("No debe solicitar cédula")

