'''
Elaborar un algoritmo que permita acumular la sumatoria de números en una variable 
teniendo en cuenta  que si el numero es mayor que 10 y par se acumula y si el numero
es impar y menor que 20 no se acumula. El algoritmo termina cuando la variable 
acumulada sea mayor o igual a  50.

INICIO
ENTERO: N, SUMA
SUMA=0
      MIENTRAS(SUMA<50) HAGA
          MOSTRAR('DIGITE UN NUMERO')
          LEER(N)
          SI(N>10) AND (N MOD2= 0) ENTONCES
               SI(N<20)ENTONCES
                        SUMA=SUMA+N.
          FIN SI
FIN MIENTRAS
MOSTRAR(' LA SUMA ES:', SUMA)
FIN
'''

suma = 0
while suma < 20:
    numero = int(input("Digite Numero: "))
    if (numero > 10) and (numero % 2 == 0):
        if numero < 20:
            suma = suma + numero # Acumulardor
print("La suma es: ", suma)