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
LEER el valor de las ventas alcanzadas

Salidas: Valor de la bonificación y Ventas realizadas

Proceso : Valor de la bonificación * Ventas realizadas
'''


print("\n")

venta_mes = int(input("Digite el valor de las ventas realizadas: "))

def bonificacion(venta_mes):
    if venta_mes < 1000000:
        bono = (venta_mes * 0)
    else:
        if (venta_mes >= 1000100) and (venta_mes <= 2500000):
            bono = (venta_mes * 0.04)
        else:
            if (venta_mes > 2500100):
                bono = (venta_mes *0.08)
    return bono

valor_bono = bonificacion(venta_mes)

print('\n')

print("La bonificacion obtenida es: ", round(valor_bono))
print('\n')


#corregido