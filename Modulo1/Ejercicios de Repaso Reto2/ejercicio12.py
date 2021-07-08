# 12. Leer un número entero de suma de los otros dos.

def digito(n):
    if int(n) < 100 and int(n) > 9:
        return True
    else:
        return False

def suma(n):
    sumar = int(n[0]) + int(n[1])
    return sumar
        
print('\n')

n1 = input("Digite un numero: ")

print('\n')

if digito(n1) == True:
    print ('La suma de los digitos del numero escrito es igua a: ',suma(n1))
else:
    print ('Digite otro número')

print('\n')

