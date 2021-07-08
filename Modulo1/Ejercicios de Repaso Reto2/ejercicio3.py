# 3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

def es_par(a):
    if len(a) >= 3:
        return "Numero no valido"
    
    if int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0:
        return "Los digitos son pares"
    else:
        return "No todos los digitos son pares"

print('\n')
numero = input("Digite un numero: ")

respuesta = es_par(numero)
print(respuesta)
print ('\n')

