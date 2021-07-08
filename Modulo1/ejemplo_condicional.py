'''
Diseñar un algoritmo que imprima el nombre del artículo, código, precio y el precio con descuento.
Si el articulo tiene código 01, el descuento es del 10%, si es código 02 el descuento es del 20%
Solo existen dos artículos


ALGORITMO
Inicio
    precio, precio_desc: float
    Leer nom_articulo, código, precio
    Si el código = 01 
        precio_desc = precio - precio*0.10
    si no
        precio_des = precio-precio*0.20
    fon si
    imprimir nom_articulo, codigo
                        precio, precio_desc
Fin

'''
print('\n')
cod_articulo=input("Digite Codigo del Articulo : ")
nom_articulo=input("Digite nombre del Articulo : ")
precio =float(input("Digite el precio del Articulo : "))

if cod_articulo == "01":
    precio_desc = precio-precio*0.10

else:
    precio_desc = precio-precio*0.20

print('\n')
print("Codigo Articulo", cod_articulo)
print("Nombre del Articulo", nom_articulo)
print("Precio Articulo",precio)
print("Precio Articulo con Descuento",precio_desc)
print('\n')