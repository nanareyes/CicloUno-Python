# 11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.

def digitos(n):
    if int(n) < 100 and int(n) > 9:
        return True
    else:
        return False


def numero_mayor(n):
    posicion = 1
    if int(n[1]) > int(n[0]):
        posicion = 2
    return posicion

print('\n')

n1 = input("Digite un numero: ")
n2 = input("Digite un numero: ")
n3 = input("Digite un numero: ") 

print('\n')


if digitos(n1) == True:
    print ('La posición mayor es: ',numero_mayor(n1))
if digitos(n2) == True:
    print ('La posición mayor es: ',numero_mayor(n2))
if digitos(n3) == True:
    print ('La posición mayor es: ',numero_mayor(n3))
else:
    print ("No es un numero valido")

print('\n')
