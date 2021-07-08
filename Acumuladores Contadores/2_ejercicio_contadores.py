"""
Diseñe un algoritmo que permita contar y sumar los números pares e impares existentes en una serie de 1 a n, siendo n un número digitado por
un usuario. 

A) Imprimir Contador de impares y pares.
b) Imprimir Suma de impares y pares.
"""

numero_actual = 1
conteo_par = 0
conteo_impar = 0
suma_par = 0
suma_impar = 0
n = float(input(" Digite un número: "))

while numero_actual <= n:
    if numero_actual % 2 == 0:
        suma_par = suma_par + numero_actual
        conteo_par = conteo_par + 1
    else:
        suma_impar = suma_impar + numero_actual
        conteo_impar = conteo_impar + 1
    numero_actual = numero_actual + 1


print(
    "La sumatoria de pares es: ",
    suma_par,
    " y la cantidad de numeros pares es: ",
    conteo_par,
)
print(
    "La sumatoria de impares es: ",
    suma_impar,
    " y la cantidad de numeros impares es: ",
    conteo_impar,
)
