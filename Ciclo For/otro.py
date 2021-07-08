Les copio el While: '''
Mientras que (While)

El Ciclo Mientras que es conocido en los lenguajes de programación como 
ciclo While, una de sus características es que verifica si la condición 
se cumple antes de ingresar al bloque de código que se va a repetir, el 
límite de ejecuciones estará dado por la condición, se ejecutará mientras 
la condición devuelva un valor lógico verdadero.

mientras  {condición}     
            acción    1  
            acción    2    
            acción    3    
             .....    
            acción  n       
     ﬁn  mientras    
    instrucción  X    

'''
x = 5
while x > 0:
    x -= 1
    print(x)
'''
Elaborar un algoritmo que permita acumular la sumatoria de números en una variable 
teniendo en cuenta  que si el numero es mayor que 10 y par se acumula y si el numero
es impar y menor que 20 no se acumula. El algoritmo termina cuando la variable 
acumulada sea mayor o igual a  100.

INICIO
ENTERO: N, SUMA
SUMA=0
      MIENTRAS(SUMA<100 )HAGA
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
            suma = suma+numero
print("La suma es:", suma)
'''
Diseñe un algoritmo que permita contar los números pares 
existentes en una serie de 1 a n, siendo n un número digitado
por un usuario

Entrada : n
Salida  : cantidad de números pares entre 1 y n
Proceso :
i = 1
cp = 0
mientras (i <= n) haga
   si ((i % 2 ) == 0
   cp += 1
   fin si
   i += 1
fin mientras
'''

n = int(input("Ingrese un numero: "))
i = 1
cp = 0

while(i <= n):
    if(i % 2 == 0):
        cp += 1

    i += 1

print(cp)
# Función
def calcularDefinitiva(p1, p2, l, t):
    defini = p1*0.3 + p2*0.35 + l*0.25 + t*0, 1
    return (defini)


# Programa principal
numeroEst = int(input("Ingrese el número de estudiantes: "))
j = 1
while(j <= numeroEst):
    nombre = input("Ingrese el nombre: ")
    par1 = float(input("parcial 1: "))
    par2 = float(input("parcial 2: "))
    lab = float(input("Laboratorios: "))
    tra = float(input("Trabajos: "))

    definitiva = (calcularDefinitiva(par1, par2, lab, tra))
    print(definitiva)
    print("la nota definitiva de ", nombre, " es: ", definitiva)
    j += 1

