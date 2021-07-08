"""
Un almacén desea saber el total de ventas por mes durante el primer trimestre del año, además desea conocer el promedio de ventas alcanzado 
durante este periodo de tiempo.
Se debe procesar n cantidad de facturas del periodo antes señalado, con la siguiente información:
1. Mes factura
2. Valor factura

Escriba una función que reciba como parámetros una lista de diccionarios que contengan la siguiente información:
3. Mes_factura: Puede ser de enero, febrero o marzo
4. valor_factura: int

Ejemplo Datos
datos: list = [
    {
        "mes_factura": "enero",
        "valor_factura": 1200000    },
    {
        "mes_factura ": "febrero",
        "valor_factura ": 3000000     },
    {
        "mes_factura ": "enero",
        "valor_factura ": 10000000     },
]

La respuesta debe retornar un diccionario con la siguiente información:
a. Total - Ventas de enero
b. Total - Ventas de febrero
c. Total - Ventas de marzo
d. Promedio de ventas en el trimestre

"""
datos: list = [
    {"mes_factura": "enero", "valor_factura": 1200000},
    {"mes_factura": "febrero", "valor_factura": 3000000},
    {"mes_factura": "marzo", "valor_factura": 10000000},
    {"mes_factura": "enero", "valor_factura": 2200000},
    {"mes_factura": "febrero", "valor_factura": 3500000},
    {"mes_factura": "enero", "valor_factura": 16000000},
    {"mes_factura": "enero", "valor_factura": 1200000},
    {"mes_factura": "marzo", "valor_factura": 3700000},
    {"mes_factura": "enero", "valor_factura": 13000000},
    {"mes_factura": "marzo", "valor_factura": 3200000},
    {"mes_factura": "febrero", "valor_factura": 5000000},
    {"mes_factura": "enero", "valor_factura": 18000000},
]


def promedio_ventas(datos: list) -> dict:
    prom_enero = 0
    prom_febrero = 0
    prom_marzo = 0
    factura_enero = 0
    factura_feb = 0
    factura_marz = 0
    total_enero = 0
    total_febrero = 0
    total_marzo = 0
    total_trimestre = 0
    facturas_totales = 0
    promedio_trimestre = 0

    for factura in datos:

        if factura["mes_factura"] == "enero":
            total_enero += factura["valor_factura"]
            factura_enero += 1
            prom_enero = round(total_enero / factura_enero)
        elif factura["mes_factura"] == "febrero":
            total_febrero += factura["valor_factura"]
            factura_feb += 1
            prom_febrero = round(total_febrero / factura_feb)
        elif factura["mes_factura"] == "marzo":
            total_marzo += factura["valor_factura"]
            factura_marz += 1
            prom_marzo = round(total_marzo / factura_marz)

        total_trimestre += factura["valor_factura"]
        facturas_totales += 1
        promedio_trimestre = round(total_trimestre / facturas_totales)

    print("\n")
    resultado = {
        "total_ventas_enero": total_enero,
        "total_ventas_febrero": total_febrero,
        "total_ventas_marzo": total_marzo,
        "venta_total_trimestre": total_trimestre,
        "promedio_ventas_enero": prom_enero,
        "promedio_ventas_febrero": prom_febrero,
        "promedio_ventas_marzo": prom_marzo,
        "promedio_trimestre": promedio_trimestre,
    }

    return resultado


print(promedio_ventas(datos))
print("\n")
