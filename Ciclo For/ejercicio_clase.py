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


def consolidar_ventas(datos: list) -> dict:
    # Tipo Ventas
    venta_credito: str = "credito"
    venta_contado: str = "contado"

    # Variable que guarda el total de ventas
    total_ventas = 0

    # total ventas a credito
    total_ventas_credito = 0

    # total ventas de contado
    total_ventas_contado = 0

    # Iterar los datos a procesar
    for item in datos:
        # Variable guarda el total de ventas
        total_ventas += item["total_factura"]
        # obtiene total venta por tipo de venta
        if item["tipo_venta"] == venta_contado:

            # Total ventas de contado
            total_ventas_contado += item["total_factura"]
        elif item["tipo_venta"] == venta_credito:

            # Total vetas a credito
            total_ventas_credito += item["total_factura"]
    # Diccionario guarda total de venta por tipo y contador por tipo de venta
    resultado: dict = {
        "total_ventas": total_ventas,
        "total_ventas_contado": total_ventas_contado,
        "total_ventas_credito": total_ventas_credito,
    }
    return resultado


datos: list = [
    {"tipo_venta": "credito", "total_factura": 10000},
    {"tipo_venta": "contado", "total_factura": 30000},
    {"tipo_venta": "credito", "total_factura": 60000},
    {"tipo_venta": "contado", "total_factura": 70000},
    {"tipo_venta": "credito", "total_factura": 90000},
    {"tipo_venta": "contado", "total_factura": 150000},
    {"tipo_venta": "contado", "total_factura": 300000},
]

print(consolidar_ventas(datos))
