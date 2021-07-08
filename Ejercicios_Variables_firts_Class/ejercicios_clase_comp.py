import os,time # se importa el modulo OS y time relacionado con el sistema operativo 
os.system ("cls") # limpia la consola

import locale

print('\n')

def venta_cam(cant):

    if cant <= 4:
      return venta * 0.125
    elif cant <= 8:
        return venta * 0.20
    elif cant > 8:
        return venta * 0.315

venta = int(input("Ingrese valor de la venta $ "))
cant = int(input("Ingrese la cantidad de camisas "))
descuento = venta_cam(cant)
print ("\x1b[1;32m"+"Ingrese valor de la venta $ ",venta, " El descuento es: $ ",descuento, "Total a pagar: $", venta-descuento )

time.sleep(10) # es el tiempo en segundos para ver la respuesta antes de ser borrada la pantalla
os.system ("cls") # limpia la consola
