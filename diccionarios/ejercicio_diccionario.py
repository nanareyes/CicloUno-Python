# supongamos que tenemos 3 valores 

# Sumatoria = Suma Ventas
# Diccionario = DicVenta
# Total Venta 
# Sumatoria = Suma Ventas
# Diccionario = DicVenta
# Total Venta 

def sumaVenta (dicVentas):
    sumatoria = 0
    sumatoria += (dicVentas['venta1'])
    sumatoria += (dicVentas['venta2'])
    sumatoria += (dicVentas['venta3'])
    totalVenta = round(sumatoria)
    return totalVenta

dicVentas = {
    "venta1": 1400000,
    "venta2": 5600000,
    "venta3": 800100
}
print('\n')
print("La venta total es: ", sumaVenta(dicVentas))
print('\n')