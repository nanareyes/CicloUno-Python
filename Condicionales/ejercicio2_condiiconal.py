# Ejercicio 1
'''

En una tienda de descuento se efectua una una promoción en la cual se hace un descuento sobre el valor de la compra total según el color de la bolita que el cliente 
saque al pagar en caja.
Si la bolita es de color blanco no ha y descuento
si la bolita es de color verde el descuento es del 10 %
si es de color amarillo el descuento es de 25%
si es de color azul un 50%
y si es roja un 100.
Escriba el valor total que el cliente debe pagar por su compra

'''

'''
Algoritmo

Inicio
Leer el valor de la compra
Si:
    Bola es blanca    0 descuento
    Bola es verde    10 descuento
    Bola amarillo    25 descuento
    Bola azul        50 descuento
    Bola roja       100 descuento


'''
compra = int(input("Digite el valor de la compra: "))
color_descuento = input("Digite el color de la bolita: ")

def valor_descuento (venta):
    if color_descuento== "amarillo":
        return (compra * 0)
    else:
        if color_descuento== "verde":
            return (compra * 0.10)
        else:
            if color_descuento == "amarillo":
                return (compra * 0.25)
            else:
                if color_descuento == "azul":
                    return (compra * 0.50)
                else:
                    if color_descuento == "rojo":
                        return (compra* 1)

valor_venta = valor_descuento (compra)

print("El valor del descuento es: ", round(valor_venta))

