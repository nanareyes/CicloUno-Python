"""
En un concesionario especializado en la venta de carros de gama baja, nuevos y usados, cuenta con cuatro vendedores, 
los cuales cuentan con una meta en su promedio de ventas trimestral. Se desea conocer el promedio de las ventas realizadas por cada vendedor en el
primer trimestre del año 2021. 
Adicionalmente se requiere saber si el promedio de ventas estipulado para cada vendedor, se cumplió de acuerdo a lo propuesto por el gerente de
ventas. 
El sistema debe imprimir un mensaje: 
    “Se alcanzó la meta del promedio de ventas en el Trimestre”, si el promedio de ventas supera los 500 millones de pesos, 

de lo contrario, el sistema debe imprimir el mensaje: 
    “No se alcanzó la meta del promedio de ventas en el Trimestre”. 
    
Se debe procesar los datos teniendo en cuenta la siguiente información:
1. Nombre del Vendedor: “Mario Correa” o “Martha Ramírez” o “Sandra Peña” o “Hugo López”
2. Mes: “Enero” o “Febrero” o “Marzo”
3. Valor Venta del mes: int

Entradas
La información de entrada esta consignada en cuatro listas:

1. vendedores
Nombre          Tipo        Estructura                                          Descripción
datos           list        [ "vendedores": str (“Mario Correa” o “Martha       La lista contiene el nombre de los cuatro vendedores en este orden: 1. Mario Correa. 2.
                            Ramírez” o “Sandra Peña” o “Hugo López”)]           Martha Ramírez 3. Sandra Peña. 4. Hugo López.”
                

2. Lista de las ventas del mes de enero

Nombre          Tipo        Estructura                                          Descripción
datos           list        [ "venta": int]                                     La lista contiene la venta realizada por cada vendedor en el mes de enero

1. Lista de las ventas del mes de febrero
Nombre          Tipo        Estructura                                          Descripción
datos           list        [ "venta": int]                                     La lista contiene la venta realizada por cada vendedor en el mes de febrero

2. Lista de las ventas del mes de marzo
Nombre          Tipo        Estructura                                          Descripción
datos           list        [ "venta": int]                                     La lista contiene la venta realizada por cada vendedor en el mes de marzo


Ejemplo de las Entradas
vendedores = [' Mario Correa ', ' Martha Ramírez ', ' Sandra Peña’, ' Hugo López ']
ventasEnero = [200000000, 300000000, 500000000, 100000000]
ventasFebrero = [120000000, 450000000, 600000000, 800000000]
ventasMarzo = [350000000, 300000000, 500000000, 700000000]

Salidas
Tipo Retorno        Descripción

str                 Vendedor:           {nombreVendedor}
                    Ventas Enero:       {recaudoEnero}
                    Ventas Febrero:     {recaudoFebrero}
                    Ventas Marzo:       {recaudoFebrero}
                    Promedio Ventas Trimestre: {promedioVentasCarros}
                    Meta:               {mensaje}
Esqueleto
def imprimir_resultados() -> str:
    pass


"""

from statistics import mean


def promedio(a, b, c) -> str:
    return round(mean([a, b, c]))


meta_venta = 500000000
vendedores = ["Mario Correa", "Martha Ramírez", "Sandra Peña", "Hugo López"]
ventasEnero = [200000000, 300000000, 500000000, 100000000]
ventasFebrero = [120000000, 450000000, 600000000, 800000000]
ventasMarzo = [350000000, 300000000, 500000000, 700000000]


promedioVentasCarros = list(map(promedio, ventasEnero, ventasFebrero, ventasMarzo))
promedioVentasTrimestre = mean(promedioVentasCarros)


def imprimir_resultados() -> str:
    for x in range(0, len(vendedores)):
        print("Vendedor: {}".format(vendedores[x]))
        print(
            "\n{} {}".format("Ventas Enero :".ljust(14), "{:,}".format(ventasEnero[x]))
        )
        print(
            "{} {}".format(
                "Ventas Febrero :".ljust(14), "{:,}".format(ventasFebrero[x])
            )
        )
        print("{} {}".format("Ventas Marzo :".ljust(14), "{:,}".format(ventasMarzo[x])))
        print(
            "{} {}".format(
                "Promedio Ventas Trimestre :".ljust(14),
                "{:,}".format(promedioVentasCarros[x]),
            )
        )
        print(
            "Meta: {}".format(
                "Se alcanzó la meta del promedio de ventas en el Trimestre"
                if promedioVentasCarros[x] > meta_venta
                else "No se alcanzó la meta del promedio de ventas en el Trimestre"
            )
        )
        print("\n{}".format("".ljust(54, "=")))


imprimir_resultados()
