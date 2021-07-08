'''
El diccionario, define una relación uno a uno entre una clave y su valor, separados con coma.

Los diccionarios en Python, al igual que las listas y las tuplas, nos permiten almacenar diferentes tipos de datos: Strings, enteros, flotantes, booleanos, tuplas, listas e inclusive otros diccionarios.

Los diccionarios son mutables, es decir, es posible modificar su longitud, podemos agregar o quitar elementos de él; de igual forma todos los valores almacenados en el diccionario pueden ser modificados.

Los Diccionarios se encuentran en otros lenguajes como arreglos asociativo.

El Diccionario en Python es una estructura de datos, tipo de dato que nos permite almacenar valores, como enteros, cadenas y funciones, entreo otros.

Los Diccionarios son contenedores, donde cada elemento (item) que contiene representa la estructura llave:valor

Cada elemento del diccionario lo identificamos con una clave (key).

Los Diccionarios se indexan con claves, cadenas y numeros pueden ser claves.

Con un par de llaves se crea un diccionario.

Una lista de pares clave:valor se añade al diccionario separados por coma (,) entre las llaves


'''

# Crear un Diccionario

movil = {"Jorge": 3120005412, "Martha": 3001234587}
print(movil)

movil = {'Jorge': 3120005412, 'Martha': 3001234587}
print(movil)

# Añadir una clave y su valor al diccionario
movil['Pedro'] = 3136214512
print(movil)

'''
El metodo dict() de lso diccionarios recibe como parametro una representacción de un diccionario y devuleve un diccionario y devuelve un diccionartio de la 
'''

del movil['Jorge']
print(movil)

#Ejemplo 1

factura = dict(nro_factura=8954, valor=150000, iva=True)
print(factura)
print(factura['valor'])
print (factura['iva'])


