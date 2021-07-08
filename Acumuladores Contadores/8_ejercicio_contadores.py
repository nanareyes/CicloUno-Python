# 8
"""
Algoritmo que permita obtener el promedio de la cantidad de números que el  usuario desee digitar, 
preguntando además si desea continuar o no.
"""
suma = 0
numero = 0
continuar = ""
cantidad = 0


while continuar != "F":
    continuar = input("Desea continuar? (T/F): ").lower()
    if continuar == "t":
        numero = float(input("Digite un número: "))
        cantidad = cantidad + 1
        suma = suma + numero

promedio = suma / cantidad

print(("El promedio de los números digitados es: "), round(promedio))
print("La cantidad de numeros digitados es: ", cantidad)
