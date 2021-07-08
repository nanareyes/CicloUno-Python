# 6
"""
Desarrolle un algoritmo que funcione como caja registradora. Que pare cuando el código del artículo se igual a *. 
Que lea:
código del articulo,
nombre y 
Precio. 
Debe calcular subtotal,iva(0,15%) y total factura.
"""


subtotal = 0
codigo = ""

while codigo != "*":
    codigo = input("Digite el codigo del artículo: ")
    if codigo != "*":
        nombre = input("Digite el nombre del artículo: ")
        precio = int(input("Digite el precio: "))
        subtotal = subtotal + precio


def valor_iva(n):
    iva = round((subtotal * 0.15), 2)
    return iva


def valor_total(n):
    total = round(subtotal - valor_iva(n))
    return total


print("Subtotal: ", subtotal)
print("Valor iva: ", valor_iva(subtotal))
print("El valor total de la factura es: ", valor_total(subtotal))
