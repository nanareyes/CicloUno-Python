# 14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.

def num(n):
    if int(n) < 10000 and int(n) > 999:
        return True
    else:
        return False


def numero_mayor(n):
    if int(n[1]) == int(n[2]):
        return True
    else:
        return False

print('\n')

numero = input("Digite un numero: ")

respuesta = num(numero)
respuesta2 = numero_mayor(numero)

if respuesta==True and respuesta2 == True:
    print("El segundo número es igual al penultimo")
else:
    print("El segundo número no es igual al penultimo")
print('\n')