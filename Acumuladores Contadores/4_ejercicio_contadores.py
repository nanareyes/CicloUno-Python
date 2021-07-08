# 4
'''
Diseñe un algoritmo que reciba números digitados por el usuario y los imprima en pantalla, el programa debe terminar cuando el usuario digite 
un número negativo.
'''
n = 0


while n >= 0:
    n = float(input("Digite un número: "))
    if n >= 0:
        print("El digitado es: ", n)
