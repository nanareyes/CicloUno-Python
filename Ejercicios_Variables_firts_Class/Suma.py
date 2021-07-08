# Algoritmo de la suma de dos numeros
'''
Se desea la suma de dos numeros enteros y presentar en pantalla
su resultado

Entradas : Num1, Num2

Proceso : La suma de los numeros --> Suma = Num1 + Num2

Salida : La suma de los numeros --> Suma
'''

'''
INICIO
 Num1, Num2, Suma: Enteros
 ESCRIBIR "Diga dos Numero:"
 LEA Num1, Num2,
 Suma <--Num1 + Num2
 ESCRIBA "la suma de dos numeros es :", suma
FIN

'''


#Suma dos numeros
numero1 = int(input("Digite el primer número:  "))
numero2 = int(input("Digite el segundo número:  "))

#Guarda el resultado de la suma de dos numeros
suma = numero1 + numero2

print("La suma de dos números es : ", suma)
