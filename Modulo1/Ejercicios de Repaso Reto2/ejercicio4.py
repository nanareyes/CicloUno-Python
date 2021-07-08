#Leer un número entero de dos dígitos menor que 20 y determinar si es primo.
'''
Algoritmo

Entrada: numeros
Proceso: < 20 y leer si es primo
Salida:  Lea un numero de dos digitos y deternimar si es primo
'''
print('\n')

def num(n):
    if n >= 10 and n <20:
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
    print("El número es de dos digitos, menor a 20 y primo")
else:
    print("El numero no cumple con los requisitos") 

print('\n')

