# 10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

def digitos_n(n):
    if int(n) >=100 and int(n) <= 999:
        return True
    else:
        return False

def es_multipl(a,b):
    if a == 0:
        return False
    elif b == 0:
        return False
    elif a % b == 0:
        return True
    else:
        return False

def es_multiplo_de_otros(numero):
    a = int (numero[0])
    b = int (numero[1])
    c = int (numero[2]) 
    if es_multipl(a,b) or es_multipl(a,c) or es_multipl(b,c) or es_multipl(b,a) or es_multipl(c,a) or es_multipl(c,b):
        return True
    else:
        return False

print('\n')

numero = input("Digite un numero: ")

respuesta = digitos_n(numero)
respuesta2 = es_multiplo_de_otros(numero)

if respuesta==True and respuesta2 == True:
    print("El número es de tres digitos, y tiene algun digito multiplo de los otros")
else:
    print("El numero no cumple con los requisitos") 
print('\n')