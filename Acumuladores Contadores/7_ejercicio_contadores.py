# 7

"""
Realizar un algoritmo para sumar consecutivamente y cuando la suma sea superior a 100 deje de pedir números y muestre el total.

"""
n = 0
suma = 0
numero = 0

while suma <= 100:
    n = float(input("Digite un número: "))
    suma = suma + n
    numero = n + 1

promedio = suma / numero

print("El total es: ", round(suma))
