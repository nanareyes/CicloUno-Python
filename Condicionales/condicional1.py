'''
CONDICIONAL SIMPLE

Algoritmo que pide un color, si se digita el color rojo en minuscula, imprime en pantalla "Tiene buen gusto !", si no, simplemente imprime "Le gusta el color" y
el nombre del color digitado:


Inicio
    Leer color
    si el color es == "rojo"
        IMPRIMIR "Tiene buen gusto!"
    Fin Si
    Imprimir "Le gusta el color : ", color
Fin
'''

color = input("Digite el color:")

if color == "rojo": 
    print("Tiene buen gusto!")

print("Le gusta el color: ",color)