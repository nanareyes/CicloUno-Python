'''
Permita calcular el total a pagar por la compra de N camisas. Si se compran entre 1 a 4 camisas se aplica un descuento del 12.5%, 
si se compra una cantidad comprendida entre 5 y 8 camisas se aplica un descuento del 20% y si se compran cantidades mayores, se aplica un descuento del 31.5% 
sobre el total de la compra. Debe imprimirse en pantalla la compra final sin descuento, monto del descuento y la compra con descuento.

'''
'''
Algoritmo

Inicio

Entradas:
Cantidad de camisas vendidas
valor descuento

Proceso
total camisas * descuento

Salidas:
Compra sin descuento
monto del descuento
Compra con descuento
'''
# (import os, time)
# (os.system("cls"))

def valor_camista(valor_ca,c):
    valor_compra = (valor_ca * c)
    return valor_compra

def descuento(v,c):
    if c <= 4:
        return (v * 0.125)
    elif c >= 5 and c <= 8:
        return (v * 0.2)
    else:
        return (v * 0.315)

print('\n')

compra = int(input("Digite el valor de la camiseta: "))
cantidad = int(input("Digite la cantidad de camisetas: "))

valor_compra = valor_camista(compra,cantidad)
resultado = descuento(valor_compra, cantidad)
print('\n')

print("El valor de la compra total es: ", round(valor_compra))
print ("El valor de descuento es:", round (resultado))
print ("El valor de la compra con descuento es: ", round(valor_compra - resultado))
print('\n')
