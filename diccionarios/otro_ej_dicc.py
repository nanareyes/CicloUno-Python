# Necesitoconocer el promedio de vetnas de la semana

def promedioVentaSemanal(dicVentas):
    sumatoria = 0
    sumatoria += (dicVentas['ventaLunes'])
    sumatoria += (dicVentas['ventaMartes'])
    sumatoria += (dicVentas['ventaMiercoles'])
    sumatoria += (dicVentas['ventajueves'])
    sumatoria += (dicVentas['ventaviernes'])
    sumatoria += (dicVentas['ventasabado'])
    totalVenta = round(sumatoria/6)
    return totalVenta

dicVentas = {
    "ventaLunes": 1400000,
    "ventaMartes": 5600000,
    "ventaMiercoles": 800100,
    "ventajueves": 930100,
    "ventaviernes": 1500100,
    "ventasabado": 500000
}
print('\n')
print("La venta total es: ", promedioVentaSemanal(dicVentas))
print('\n')