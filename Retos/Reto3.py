"""
Una ferretería desea conocer el total de las ventas en general y el consolidados de ventas de contado y crédito, se debe procesar n cantidad de facturas 
con la siguiente información:
1. Tipo Venta
2. Valor Factura
Escriba una función que reciba como parámetros una lista de diccionarios que contengan la
siguiente información:
1. tipo_venta: “credito” o “contado”
2. valor_factura: int
La respuesta de retornara en un diccionario con la siguiente estructura:
• {total_ventas: int, total_ventas_contado: int, total_ventas_credito: int}


Factura 1 {
"tipo_venta": "credito",
"total_factura": 85000
}
Factura 2 {
"tipo_venta": "contado",
"total_factura": 100000
}
Factura 3 {
"tipo_venta": "credito",
"total_factura": 20000
}
Return {
"total_ventas": 205000,
"total_ventas_contado": 100000
"total_ventas_credito": 105000
}

Entradas
Nombre: datos
Tipo : list
Estructura [{ "tipo_venta": str (‘’contado” o “credito”), "total_factura": int }]
Descripción: La lista contiene n cantidad de diccionarios con la información de las ventas realizadas soportadas con las facturas

Salidas
Tipo del Retorno : dict

Estructura { 
"total_ventas": int,
"total_ventas_contado": int,
"total_ventas_credito": int
}

Descripción: El diccionario contiene el total de ventas en general, total de ventas a credito y total de ventas a contado

Esqueleto
def consolidar_ventas(datos: list) -> dict:

"""

datos: list = [
    {"tipo_venta": "credito", "total_factura": 85000},
    {"tipo_venta": "contado", "total_factura": 100000},
    {"tipo_venta": "credito", "total_factura": 20000},
]


def consolidar_ventas(datos: list) -> dict:
    total_ventas = 0
    total_ventas_contado = 0
    total_ventas_credito = 0

    for ventas in datos:
        total_ventas += ventas["total_factura"]
        if ventas["tipo_venta"] == "contado":
            total_ventas_contado += ventas["total_factura"]
        elif ventas["tipo_venta"] == "credito":
            total_ventas_credito += ventas["total_factura"]

    resultado = {
        "total_ventas": total_ventas,
        "total_ventas_contado": total_ventas_contado,
        "total_ventas_credito": total_ventas_credito,
    }
    return resultado


print(consolidar_ventas(datos))
