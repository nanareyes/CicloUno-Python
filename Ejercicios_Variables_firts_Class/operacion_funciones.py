# Funcion que realiar la suma de dos numeros
''' son las instrucciones'''

def sumar(a,b,c,d):

   s = (a + b + c + d)

   return s

def resta(a,b):
   r = a - b
   return r

def multiplicar(a,b):
   m = a * b
   return m

def dividir(a,b):
   d = a / b
   return d

#Aquí inicia la aplicación
numero1 = int(input("Digite el primer numero : "))
numero2 = int(input("Digite el segundo numero : "))
numero3 = int(input("Digite el tercer numero :"))
numero4 = int(input("Digite el cuarto numero :"))

suma = sumar(numero1, numero2, numero3, numero4)
restar = resta(numero1, numero2)
multiplica = multiplicar(numero1, numero2)
divide = dividir(numero1, numero2)


print("a + b + c + d =", suma)
print("a - b =", restar)
print("a * b =", multiplica)
print("a / b =", divide)