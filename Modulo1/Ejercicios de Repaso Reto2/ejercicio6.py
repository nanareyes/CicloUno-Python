# 6. Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.


print("\n")


def numero(n):
    if int(n) >= 10 and int(n) < 100:
        if int(n[0]) == int(n[1]):
            return True
    else:
        return False


valor_n = input("Digite un número: ")

solucion = numero(valor_n)

if solucion == True:
    print("El número tiene dos digitos iguales")
else:
    print("El numero no tiene digitos iguales")

print("\n")
