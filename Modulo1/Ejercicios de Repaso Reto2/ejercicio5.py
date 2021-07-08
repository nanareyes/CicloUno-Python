# 5. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.


print('\n')


def esprimo(n):
    n_abs = abs(n) 
    for i in range(2, n_abs):
        if n_abs % i == 0:
            return False
    return True


def esnegativo(n):
    if n > -100 and n < -9:
        return True
    else:
        return False

numero = int(input("Digite un número: "))
es_numero_primo = esprimo(numero)
es_negativo= esnegativo(numero)

if es_numero_primo == True and es_negativo == True:
    print("El número es primo y además negativo")
else:
    print("El número no es primo y negativo al mismo tiempo")




