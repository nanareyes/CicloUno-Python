'''
Desarrolle un algoritmo que permita leer un valor cualquiera N y escriba si dicho número es par o impar.

Algoritmo

Inicio
    Digite un valor n
    si n/ 2 = numero entero entonces 
        El numero es par

    si no
        El numero es impar

Fin
'''

a = int(input("Digite un numero: "))
if a % 2 ==0:
    print("es par")
else:
    print("es impar")

print("El numero ", + int(str(a)))


