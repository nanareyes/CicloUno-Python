'''
#Preguntar a Fredy gil

numero = input("Digite un número: ")
f = True;
for p in range(0, len(numero)):
    if int(numero[p])%2==1:
        f = False
        break
if f:
    print("Todos los digitos son pares")
else:
    print("No todos los digitos son pares")

'''




'''
n= int(input("Digite un numero: "))
for n in range (n):
    for x in range (n):
        if (n % x == 0):
            print(n ("es igual a"), x, '*', n/x)
    else:
        print( n, "es un numero primo")

'''


'''
numero = int(input("Digite un número: "))

def leer(n):
    if n % 2 == 0:
        return n
    else:
        ("")
'''
'''
def repetir_funciones():
    imprime_cosas()
    imprime_cosas()

def imprime_cosas():
    print("La clase esta genial")
    print("Python es lo maximo")




repetir_funciones()
'''
# No entendí elejercicio de abajo
'''
def consultar_nom_genero(letra_genero): pass
type(consultar_nom_genero)

consultar_nom_genero("M")
print(consultar_nom_genero)
'''
#otra funcion
'''
def otra_suma(n1, n2):
    print(n1 + n2)
    return n1 + n2

resul=otra_suma(3,4)

print(resul)
'''
#otra
'''
def nombre_completo (nombre, apellido):
    nombre = nombre, apellido
    print(nombre)

nombre_completo('Diana', 'Reyes')
'''

#otra
'''
def saludar(nombre, mensaje='Hello'):
    print(mensaje, nombre)
saludar(mensaje='Buen día', nombre='Caro')
'''

def saludo(cadena):
    return "Hola {}! ¡Como estas".format(cadena)
    
