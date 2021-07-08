"""
Un almacen de jugueteria desea conocer el total de las ventas en general y el consolidado de ventas de contado y crédito, 
se debe procesar n cantidad de facturas con la siguiente información:

ENTRADAS
tipo de venta : credito o contado
Valor factura

SALIDA
1. Total ventas
2. Total ventas de Contado
3. Total ventas de Credito
"""
datos: list = [
    {"tipo_venta": "credito", "total_factura": 10000},
    {"tipo_venta": "contado", "total_factura": 30000},
    {"tipo_venta": "credito", "total_factura": 60000},
    {"tipo_venta": "contado", "total_factura": 70000},
    {"tipo_venta": "credito", "total_factura": 90000},
    {"tipo_venta": "contado", "total_factura": 150000},
    {"tipo_venta": "contado", "total_factura": 300000},
]


def consolidado_ventas(datos: list) -> dict:

    total_venta_contado = 0
    total_venta_credito = 0
    total_ventas = 0

    for venta in datos:
        if venta["tipo_venta"] == "contado":
            total_venta_contado = total_venta_contado + venta["total_factura"]
        else:  # Puedo hacerlo con elif con esta definición: venta["tipo_venta"] == "credito"
            total_venta_credito = total_venta_credito + venta["total_factura"]

    total_ventas = total_venta_contado + total_venta_credito

    resultado = {
        "total_ventas": total_ventas,
        "total_ventas_credito": total_venta_credito,
        "total_ventas_contado": total_venta_contado,
    }
    return resultado


print("\n")

print(consolidado_ventas(datos))

print("\n")
