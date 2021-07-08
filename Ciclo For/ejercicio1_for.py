# 1. Introducir 10 números y sumar solo los números pares. Imprimir la sumatoria


suma_pares = 0

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
print("La suma de los número pares es: ", suma_pares)
