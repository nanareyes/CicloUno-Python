# 5
'''
Diseñe un algoritmo que reciba números digitados por el usuario y al final imprima la suma de los números digitados, 
el programa debe terminar cuando el usuario digite 0 (cero)

'''


numero = 1
suma = 0


while numero != 0 :
    numero =  float(input("digite un número: "))
    suma = suma + numero

#respuesta
print(" La suma total es: ", (round(suma)))
