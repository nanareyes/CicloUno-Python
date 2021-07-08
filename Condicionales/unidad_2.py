# leer 2 numeros difernes e indicar cual es el mayor de ellos 

def cual_es_mayor(a,b):
    if(a > b):
        return a
    else:
        return b

#La aplicación inicia aquí
print('\n')
a = int(input("Digite Numero 1 : "))
b = int(input("Digite numero 2 : "))

respuesta = cual_es_mayor(a,b)
print('\n')
print ("El numero mayor es : ", respuesta)
print('\n')