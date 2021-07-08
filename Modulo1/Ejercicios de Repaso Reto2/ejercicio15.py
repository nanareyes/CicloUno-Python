#15. Leer un número entero y determinar si es múltiplo de 7.

def es_multipl(a):
    if a == 0:
        return False
    elif a % 7 == 0:
        return True
    else:
        return False

print('\n')

numero = int(input("Digite un numero: "))

respuesta = es_multipl(numero)

if respuesta == True:
    print("El número es multiplo de 7")
else:
    print("El numero no es multiplo de 7") 
print('\n')