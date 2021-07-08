# 13. Leer un número entero menor que 50 y positivo y determinar si es un número primo.

print('\n')

def num(n):
    if n >= 10 and n <50:
        return True
    else:
        return False

def esprimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite un numero: "))

respuesta = num(numero)
respuesta2 = esprimo(numero)

if respuesta==True and respuesta2 == True:
    print("El número es de dos digitos, menor a 50, positivo y primo")
else:
    print("El numero no cumple con los requisitos") 

print('\n')