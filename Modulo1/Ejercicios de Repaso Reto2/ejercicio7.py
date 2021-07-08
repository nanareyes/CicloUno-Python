# 7. Leer dos números enteros y determinar cuál es el mayor.
print('\n')
print("SE SOLICITAN DOS NUMEROS")
def numero_mayor(a,b):
    if a == b:
        print ('Los numeros son iguales')
    elif a > b:
        print ("El numero ",a, "es mayor que ", b)
    else:
        print ("El numero ",b, "es mayor que ", a)


a= int(input ('Digite el primer numero: '))
b = int(input('Digite el segundo numero: '))

numero_mayor(a,b)