# 4. Leer 10 números e imprimir la sumatoria de los pares, impares y la suma total de los 10 números.

suma_pares = 0
suma_impares = 0


for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
suma_total = suma_impares + suma_pares

print("La suma de los número pares es: ", suma_pares)
print("La suma de los número impares es: ", suma_impares)
print("La suma total es: ", suma_total)

"""


suma_pares = 0
suma_impares = 0
suma_total = 0

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    suma_total = suma_total + numero
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
suma_total = suma_impares + suma_pares

print("La suma de los número pares es: ", suma_pares)
print("La suma de los número impares es: ", suma_impares)
print("La suma total es: ", suma_total)

"""
