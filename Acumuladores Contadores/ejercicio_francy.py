"""
Diseñe un algoritmo que permita contar y sumar los números pares e impares existentes en una serie de 1 a n, siendo n un número digitado por
un usuario. 

A) Imprimir Contador de impares y pares.
b) Imprimir Suma de impares y pares.
"""

# Hacerlo pero colocando la cantidad de números que se quiere digitar....


def contador_suma(conpar, conimpar, sumpar, sumimpar):
    j = 1
    while j <= numero:
        num = int(input(" Ingrese un número mayor a cero: "))
        if num <= 0:
            print("Recuerda ingresar un número mayor que cero")
        else:
            if num % 2 == 0:
                conpar += 1
                sumpar = sumpar + num
            else:
                conimpar += 1
                sumimpar = sumimpar + num
            j += 1
    return f"La cantidad de numeros pares son: {conpar} \n La cantidad de números Imoares son: {conimpar}\n, la suma de números impares es: {sumimpar}, y la suma de numeros pares es: {sumpar}"


numero = int(input("Cuántos números desea ingresar?: "))
conpar, conimpar, sumpar, sumimpar = 0, 0, 0, 0
print(contador_suma(conpar, conimpar, sumpar, sumimpar))
