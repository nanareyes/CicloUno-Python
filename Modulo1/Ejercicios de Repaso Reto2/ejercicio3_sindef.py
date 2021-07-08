# 3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
print('\n')


def son_pares(n):
    if int(n) < 10 or int(n) > 99:
        return("Numero no valido")

    if int(n[0])%2 == 0 and int(n[1]) % 2 == 0:
        return "Todos los digitos son pares"
    else:
        return "No todos los digitos son pares"


numero = input("Digite un numero: ")

respuesta = son_pares(numero)
print(respuesta)
print('\n')

