# Leer dos números y decir si son iguales o no
'''
Si a es igual a b = un mensaje
Si a no es igual a b = otro mensaje


'''

def cual_es_igual(a,b):
    if (a == b):
        return "Si"
    else:
        return "No"

#Aquí comienza la aplicación
print('\n')
a =int(input("Escriba el valor de A : "))
b =int(input("Escriba el valor de B : "))
respuesta = cual_es_igual(a,b)
print("A es igual a B", respuesta)
print('\n')