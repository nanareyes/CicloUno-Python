# 9. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.

def digitos(n):
    if int(n) < 1000 and int(n) > 99:
        return True
    else:
        return False


def numero_mayor(n):
    posicion = 1
    if int(n[1]) > int(n[0]):
        posicion = 2
    if int(n[2]) > int(n[1]):
        posicion = 3
    return posicion

print('\n')

numero = input("Digite un numero: ")

if digitos(numero) == True:
    print ('La posición mayor es: ',numero_mayor(numero))
else:
    print ("No es un numero valido")

print('\n')

