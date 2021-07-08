# 3. Leer 4 números. Imprimir la sumatoria y su promedio.

suma = 0

for i in range(4):
    numero = int(input("Ingrese un numero: "))
    suma = suma + numero
    promedio = suma / 4
print("La suma de los número pares es: ", suma, " y su promedio es: ", round(promedio))
