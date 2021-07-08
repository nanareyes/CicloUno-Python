#1. Leer un número entero y determinar si es un número terminado en 4.


numero = int(input("Digite un numero entero: "))
digito = numero % 10

if digito == 4:
    print("El numero ingresado termina en 4")
else:
    print("El numero ingresado no termina en 4")
