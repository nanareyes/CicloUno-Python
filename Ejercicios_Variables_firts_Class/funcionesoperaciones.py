'''
Desarrollar un algoritmo que permita convertir calificaciones numericas a letras, segun la siguiente tabla:
Se asume que la nota es un número y está comprendido entre 1 y 20

A = 19 y 20
B = 16, 17 y 18
C = 13, 14 y 15
D = 10, 11 y 12
E = 1 hasta el 9
'''

nota = int(input("Digite la nota: "))

if (nota >= 1) and (nota <= 9):
    print("La calificación es: A")
else:
    if (nota >=10) and (nota <= 12):
        print("La calificación es: B")
    else:
        if (nota >= 13) and (nota <= 15):
            print("La calificación es: C")
        else:
            if (nota <= 16) and (nota <= 18):
                print("La calificación es: D")
            else:
                print("La calificación es: E")
