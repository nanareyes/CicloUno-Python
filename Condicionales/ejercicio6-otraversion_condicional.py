'''
Elabora un algoritmo que permita ingresar el monto de la venta alcanzada por un vendedor durante un mes,
se debe calcular la bonificación (%) que tiene derecho de acuerdo a la siguiente tabla:

0 - 1000.000           Bonificación    0
1.000.100 - 2.500.000  Bonificacion 0.04
2.500.100 o más        Bonificación 0.08

Imprimir venta realizada en el mes y la bonificación obtenida
'''

'''
ALGORITMO

Inicio
Entradas: el valor de las ventas alcanzadas

Salidas: Valor de la bonificación y Ventas realizadas

Proceso : Valor de la bonificación * Ventas realizadas
'''
print("\n")

ventas = int(input("Digite las ventas del mes: "))

print("\n")
def bonificacion_ventas(mes):
    if (ventas <= 1000000):
        bono = (ventas * 0)
    else:
        if (ventas <= 2500000): 
            bono= (ventas * 0.04)
        else:
            bono = (ventas * 0.08)
    return bono
        
resultado= bonificacion_ventas(ventas)
print("El valor de las ventas mensuales es: $",ventas)
print ("La bonificacion es: $ %.0f"% resultado)
print("\n")
