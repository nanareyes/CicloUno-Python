# 8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos.

def numero_entero(numero1,numero2):
    if int(numero1) > 9 and int(numero2) < 100:
        return True
    elif int(numero1) > 9 and int(numero2) < 100:
        return True
    else:
        return False

def suma(numero1, numero2):
    a = int (numero1[0])  
    b = int (numero1[1])
    
    c = int (numero2[0]) 
    d = int (numero2[1])
    sumar = a + b + c + d
    return sumar

print('\n')

numero1 = input('Digite un número: ')
numero2 = input('Digite otro número: ')

respuesta1= numero_entero(numero1, numero2)
respuesta2= suma(numero1, numero2)

if respuesta1 == True:
    print (('La suma de los digitos es: '), respuesta2)
else:
    print ('Digite otro número')


print('\n')