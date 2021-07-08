# Leer dos números y decir si son iguales o no
'''
Si a es igual a b = un mensaje
Si a no es igual a b = otro mensaje


'''

def cual_es_igual(a,b):
    if (a == b):
        print("A es igual a B")
    else:
        print("A no es igual a B")

#Aquí comienza la aplicación
print('\n')
a =int(input("Escriba el valor de A : "))
b =int(input("Escriba el valor de B : "))
cual_es_igual(a,b)
print('\n')