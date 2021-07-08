
'''
Diseñe un algoritmo que permita contar los números pares existentes en una serie de 1 a n, siendo n un número digitado por un usuario

Entrada : n

Salida  : cantidad de números pares entre 1 y n

Proceso :
i = 1
contador_pares = 0
mientras (i <= n) haga
   si ((i % 2 ) == 0
     contador_pares += 1
   fin si
   i += 1
fin mientras
'''
numero = int(input("Ingrese un numero de veces: "))
i = 1
contador_pares = 0

while (i <= numero):
    if(i % 2 == 0):
        contador_pares += 1 # contador
    
    i +=1

print(contador_pares)
